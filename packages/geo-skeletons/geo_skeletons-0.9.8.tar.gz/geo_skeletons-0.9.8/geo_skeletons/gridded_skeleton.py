import numpy as np
from .skeleton import Skeleton
from .point_skeleton import PointSkeleton
from .distance_functions import lon_in_km, lat_in_km


class GriddedSkeleton(Skeleton):
    """Gives a gridded structure to the Skeleton.

    In practise this means that:

    1) Grid coordinates are defined as x,y / lon,lat.
    2) Methods x(), y() / lon(), lat() will return the vectors defining the grid.
    3) Methods xy() / lonlat() will return a list of all points of the grid
    (i.e. raveled meshgrid).
    """

    def is_gridded(self) -> bool:
        return True

    def _initial_coords(self) -> list[str]:
        """Initial coordinates used with GriddedSkeletons. Additional coordinates
        can be added by decorators (e.g. @add_time).
        """
        return ["y", "x"]

    def _initial_vars(self) -> dict:
        """Initial coordinates used with GriddedSkeletons. Additional variables
        can be added by decorator @add_datavar.
        """
        return {}

    def lonlat(
        self,
        mask: np.ndarray = None,
        order_by: str = "lat",
        native: bool = False,
        strict: bool = False,
        **kwargs,
    ) -> tuple[np.ndarray, np.ndarray]:
        """Returns a tuple of lon and lat of all points.
        If strict=True, then None is returned if grid is sperical.

        mask is a boolean array (default True for all points)
        order_by = 'y' (default) or 'x'
        """

        if self.is_cartesian() and (strict or self.strict) and (not native):
            return None, None

        if mask is None:
            mask = np.full(super().size("spatial", **kwargs), True)
        mask = mask.ravel()

        x, y = self._native_xy(**kwargs)

        if not self.is_cartesian() or native:
            return x[mask], y[mask]

        # Only convert if skeleton is Cartesian and native output is not requested
        points = PointSkeleton(x=x, y=y)
        points.set_utm(self.utm(), silent=True)

        return points.lonlat(mask=mask)

    def xy(
        self,
        mask: np.ndarray = None,
        order_by: str = "y",
        native: bool = False,
        strict: bool = False,
        normalize: bool = False,
        **kwargs,
    ) -> tuple[np.ndarray, np.ndarray]:
        """Returns a tuple of x and y of all points.
        If strict=True, then None is returned if grid is sperical.

        mask is a boolean array (default True for all points)
        order_by = 'y' (default) or 'x'
        """

        if not self.is_cartesian() and (strict or self.strict) and (not native):
            return None, None

        if mask is None:
            mask = np.full(super().size("spatial", **kwargs), True)
        mask = mask.ravel()

        x, y = self._native_xy(**kwargs)

        if self.is_cartesian() or native:
            return x[mask], y[mask]

        # Only convert if skeleton is not Cartesian and native output is not requested
        points = PointSkeleton(lon=x, lat=y)
        points.set_utm(self.utm(), silent=True)

        return points.xy(mask=mask)

    def _native_xy(self, **kwargs) -> tuple[np.ndarray, np.ndarray]:
        """Returns a tuple of native x and y of all points."""

        x, y = np.meshgrid(
            super().x(native=True, **kwargs), super().y(native=True, **kwargs)
        )

        return x.ravel(), y.ravel()

    def set_spacing(
        self,
        dlon: float = 0.0,
        dlat: float = 0.0,
        dx: float = 0.0,
        dy: float = 0.0,
        dm: float = 0.0,
        dnmi: float = 0.0,
        nx: int = 0,
        ny: int = 0,
        floating_edge: bool = False,
    ) -> None:
        """Defines longitude and latitude vectors based on desired spacing.

        Options (priority in this order)
        nx, ny [grid points]:   Grid resolution is set to have nx points in
                                longitude and ny points in latitude direction.

        dlon, dlat [deg]:       Grid spacing is set as close to the given resolution
                                as possible (edges are fixed).

        dm [m]:                 Grid spacing is set close to dm metres.

        dnmi [nmi]:            Grid spacing is set close to dnmi nautical miles.

        dx, dy [m]:             Grid spacing is set as close as dx and dy metres as
                                possible.

        Set floating_edge=True to force exact dlon, dlat
        and instead possibly move lon_max, lat_max slightly
        to make it work (only compatibel with native coordinates).

        """

        def determine_nx_ny(nx, ny, dx, dy, dm, dlon, dlat, dnmi):
            x_end = self.edges("x", native=True)[1]
            y_end = self.edges("y", native=True)[1]

            if nx and ny:
                return int(nx), int(ny), x_end, y_end

            if dnmi:
                if self.is_cartesian():
                    dm = dnmi * 1850
                else:
                    dlat = dnmi / 60
                    x_km = lon_in_km(np.median(self.lat()))
                    y_km = lat_in_km(np.median(self.lat()))
                    dlon = dlat * (y_km / x_km)

            if dlon and dlat:
                nx = np.round((self.edges("lon")[1] - self.edges("lon")[0]) / dlon) + 1
                ny = np.round((self.edges("lat")[1] - self.edges("lat")[0]) / dlat) + 1
                if floating_edge:
                    if self.is_cartesian():
                        raise Exception(
                            "Grid is cartesian, so cant set exact dlon/dlat using floating_edge!"
                        )
                    x_end = self.edges("lon")[0] + (nx - 1) * dlon
                    y_end = self.edges("lat")[0] + (ny - 1) * dlat
                return int(nx), int(ny), x_end, y_end

            if dm:
                dx = dm
                dy = dm

            if dx and dy:
                nx = np.round((self.edges("x")[1] - self.edges("x")[0]) / dx) + 1
                ny = np.round((self.edges("y")[1] - self.edges("y")[0]) / dy) + 1
                if floating_edge:
                    if not self.is_cartesian():
                        raise Exception(
                            "Grid is spherical, so cant set exact dx/dy using floating_edge!"
                        )
                    x_end = self.edges("x")[0] + (nx - 1) * dx
                    y_end = self.edges("y")[0] + (ny - 1) * dy
                return int(nx), int(ny), x_end, y_end

            raise ValueError(
                "Give a combination of nx/xy, dlon/dlat, dx/dy or dm or dmi"
            )

        nx, ny, native_x_end, native_y_end = determine_nx_ny(
            nx, ny, dx, dy, dm, dlon, dlat, dnmi
        )

        # Unique to not get [0,0,0] etc. arrays if nx=1
        x_native = np.unique(np.linspace(self.x(native=True)[0], native_x_end, nx))
        y_native = np.unique(np.linspace(self.y(native=True)[0], native_y_end, ny))

        if self.is_cartesian():
            x = x_native
            y = y_native
            lon = None
            lat = None
        else:
            lon = x_native
            lat = y_native
            x = None
            y = None
        self._init_structure(x, y, lon, lat)

    def __repr__(self) -> str:
        string = "grid = GriddedSkeleton"

        x0, x1 = self.edges("x", native=True)
        y0, y1 = self.edges("y", native=True)
        string += f"({self.x_str}=({x0},{x1}), {self.y_str}=({y0},{y1}))\n"

        string += f"grid.set_spacing(nx={self.nx()}, ny={self.ny()})\n"
        if self.is_cartesian():
            utm_number, utm_zone = self.utm()
            string += f"grid.set_utm(({utm_number}, '{utm_zone}'))"

        return string
