from types import SimpleNamespace
import numpy as np

from darray import DataSource, Projection


class DataSource2DFunction(DataSource):
    def __init__(self, func):
        """
        Parameters
        ----------
        func : callable
            A callable with the signature


                def func(x: Array[1, n], y: Array[m, 1]) -> Array[m, n]:
                    ...

            That computes a function on a even grid
        """
        self._func = func

    def queryArray(self, ax, *args):
        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()

        # TODO handle cases were we don't know this or it has changed
        ax_size = ax.get_window_extent()
        xcount = int(np.round(ax_size.width))
        ycount = int(np.round(ax_size.height))
        x_half_pix_size = np.abs(xmax - xmin) / xcount / 2
        y_half_pix_size = np.abs(ymax - ymin) / ycount / 2

        payload = self._func(
            np.linspace(xmin, xmax, xcount).reshape(1, -1),
            np.linspace(ymin, ymax, ycount).reshape(-1, 1),
        )

        data = Projection(payload, 1, [ycount, xcount])

        extent = Projection(
            [
                xmin - x_half_pix_size,
                xmax + x_half_pix_size,
                ymin - y_half_pix_size,
                ymax + y_half_pix_size,
            ],
            1,
            (4),
        )
        return SimpleNamespace(data=data, extent=extent)


class DataSource1DFunction(DataSource):
    def __init__(self, func):
        """
        Parameters
        ----------
        func : callable
            A callable with the signature


                def func(x: Array[n]) -> Array[n]:
                    ...

            That computes a function over a given range
        """
        self._func = func

    def queryXY(self, ax, *args, xdim=1):
        xmin, xmax = ax.get_xlim()
        ax_size = ax.get_window_extent()
        xcount = int(np.round(ax_size.width))
        x = np.linspace(xmin, xmax, xcount).reshape(1, -1)
        y = self._func(x)
        yp = Projection([y], 1, [y.shape])

        # data source knows the sampling rate

        xp = Projection([x], 1, [x.shape])

        return SimpleNamespace(x=xp, y=yp)

    def queryArray(self, ax, *args):
        xmin, xmax = ax.get_xlim()
        ax_size = ax.get_window_extent()
        xcount = int(np.round(ax_size.width))
        x_half_pix_size = np.abs(xmax - xmin) / xcount / 2

        payload = self._func(np.linspace(xmin, xmax, xcount)).reshape(1, -1)

        data = Projection(payload, 1, [1, xcount])

        extent = Projection(
            [xmin - x_half_pix_size, xmax + x_half_pix_size, -0.5, 0.5], 1, (4),
        )
        return SimpleNamespace(data=data, extent=extent)
