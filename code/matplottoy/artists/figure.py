from types import SimpleNamespace
import matplotlib.image as mimage
from matplotlib.patches import Rectangle
from matplotlib.backends.backend_agg import RendererAgg
import matplotlib.transforms as mtransforms
import matplotlib.path as mpath
import matplotlib.colors as mcolors
import numpy as np


def print_png(figure, filename_or_obj):
    # the object that knows how to go from retinal space -> final render
    renderer = RendererAgg(figure.w, figure.h, figure.dpi)
    # call draw method on
    figure.draw(renderer)

    # as a sideeffect of the draw (!) the renderer now holds a rasterized
    # version of the figure
    mimage.imsave(
        filename_or_obj,
        renderer.buffer_rgba(),
        format="png",
        origin="upper",
        dpi=figure.dpi,
    )


class MiniFigure:
    def __init__(self, size, *children):
        self.w, self.h, self.dpi = size
        self.children = children

    def draw(self, renderer):
        # the Agg renderer starts with (0, 0, 0, 0) in every
        # pixel, put a hatched background in place
        Rectangle(
            xy=(0, 0),
            width=self.w,
            height=self.h,
            facecolor="w",
            edgecolor=".9",
            linewidth=5,
            hatch="x",
        ).draw(renderer)
        # now draw all of our children
        for c in self.children:
            c.draw(renderer)

    def set_canvas(self, canvas):
        self.canvas = canvas


class MiniLine:
    def __init__(self, xdata, ydata, *, linewidth=5, color="CO"):
        self.xdata = xdata
        self.ydata = ydata
        self.linewidth = linewidth
        self.color = color

    def draw(self, renderer):
        # make the Path object
        path = mpath.Path(np.vstack([self.xdata, self.ydata]).T)
        # make an configure the graphic context
        gc = renderer.new_gc()
        gc.set_foreground(mcolors.to_rgba(self.color), isRGBA=True)
        gc.set_linewidth(self.linewidth)
        # add the line to the render buffer
        renderer.draw_path(gc, path, mtransforms.IdentityTransform())


if __name__ == 'main':
    print_png(
        MiniFigure(
            (500, 400, 100),
            MiniLine(
                # these are in pixels
                range(500),
                150 + 100 * (np.sin(np.linspace(0, 6 * np.pi, 500))),
                linewidth=5,
                color="C3",
            ),
            MiniLine(
                # these are in pixels
                range(500),
                150 + 100 * (np.cos(np.linspace(0, 6 * np.pi, 500))),
                linewidth=5,
                color="C1",
            ),
        ),
        "/tmp/test.png",
    )
