
def make_bars(xval, xoff, yval, yoff):
    return [[(x, y), (x, y+yo), (x+xo, y+yo), (x+xo, y), (x, y)] 
            for (x, xo, y, yo) in zip(xval, xoff, yval, yoff)]



class BarVerticalArtist:

"""rewritten as a function that's fullly curried to close over data subsetting, 
also closes over tau

def data_fiber()
    def nu()


"""
    def __init__(self, position, height, floor, width, facecolor, edgecolor, linewidth, linestyle):
        ### F->V maps need to be fixed here, but use fiber name instead of function
        self.position = position #(string, callable)
        self.height = height
        self.floor = floor
        self.width = width
        self.facecolor = facecolor
        self.edgecolor = edgecolor
        self.linewidth = linewidth
        self.linestyle = linestyle

    def __call__(self, data): 
        # need someway to pass in data rather than k - sin vs cos, different fruit df
        # do this by pulling tau here, 
        self.data = None

        ### returns new artist that clos

    
    def draw(self, renderer): #Q?
        # xi has to happen in draw b/c of axes refereshing?

        xval = self.position[1](self.position[0](k)())
        xoff = self.width[1](self.width[0](k)())
        yval = self.floor[1](self.floor[0](k)())
        yoff = self.height[1](self.height[0]())

        boxes = make_bars(xval, xoff, yval, yoff)
        color = self.facecolor[]#

# Artist - (Q \circ \nu \cir) tau 
# fiber = R^{2}, Artist  LineR^{2}, linear(cos), linear(sin)
# fruitArtist(df1), fruitartist(df2)

class ArtistDraw:
    """sort out which renderer.draw function I need for bars"""
    def __init__(self, artist):
        pass

    def draw(self, renderer):
        #close over artist, returns something I can pass to the render
        # Qhat/Q
        pass


#
a1 = (
Artist()
.compose_with_nu(color=("name", CatMap))
.compose_with_nu(x=("x", x_transform))
.compose_with_nu(color=("age", CatMap))
.compose_with_tau(section)
.query(bounding_box)
) # .render(renderer)
a2 = (
Artist()
.compose_with_nu(color=("name", CatMap), x=("x", x_transform))
.compose_with_tau(section)
.query(bounding_box)
# .fullfill_promise(x_transform)
) # .draw(renderer)

artist_template = Artist().compose_with_nu(color=("name", CatMap), x=("x", x_transform))

a3 = artist.compose_with_tau(sectionA)
a4 = artist.compose_with_tau(sectionB)
a1 = (
Artist()
.compose_with_nu(color=("name", CatMap))
.compose_with_nu(x=("x", x_transform))
.compose_with_nu(color=("age", CatMap))
.compose_with_tau(section)
)

a1_zoomed = a1.query(smaller_bounding_box)

draw(render, data_bounding_box, compose_with_tau(section, compose_with_nu(...)))


class ShimArtist(mpl.Artist):
def __init__(self, hannahs_thing):
self._actual = hannahs_thing

def draw(self, rendrer):
self.ax.get_xlim()
...
self._actual(render, *stuff, **more_stuff)
# self._actual.draw(render, *stuff, **more_stuff)

BarArtist:()