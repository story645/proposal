from collections import namedtuple
import copy

import numpy as np 

from matplotlib import rcParams

import matplotlib.artist as martist
import matplotlib.path as mpath
import matplotlib.transforms as mtransforms

from matplottoy.artists import utils
from matplottoy.encoders import mtypes

# mu = \nu \circ \tau 
Mu = namedtuple('Mu', ['nu', 'F'])
class QHatData: 
#is bad name for this since this is more than just qhat
    def __init__(self, graphic):
        self.graphic = graphic
        self.section = None

    def compose_with_tau(self, section): #doesn't need to be there
        # do I care about bounds yet? or only at draw time?
        new = copy.copy(self)
        new.section = section
        return new

    def query(self, data_bounds=None):
        return self.section.local_section(data_bounds)
        # section.view, #xi seperates nicly 


class QHatGraphic:
    def make_mu(self, bounds):
        pass
    @staticmethod
    def qhat():
        pass

class Bar(QHatGraphic): 
    #what are the 
    P = {'position', 'height', 'floor', 'width', 
         'facecolor', 'edgecolor', 'linewidth', 'linestyle'}
    
    def __init__(self, orientation='v', V=None):
        # F->V maps need to be fixed here, but use fiber name instead of function
        self.orientation = orientation
        self.V = {k:Mu(None,None) for k in self.P}


    @property
    def V(self):
        return self._V.copy()

    @V.setter
    def V(self, mus):
        assert mus.keys() <= self.P
        self._V = mus
        
    def compose_with_nu(self, **kwargs):
        #trying to sort out how to not lose existing specs
        # also maybe type checking here? (Is this nu valid for this fiber?)
        nus = self.V
        nus.update(kwargs)
        new = copy.copy(self)
        new.V = nus
        return new

    def make_mu(self, restricted_tau): #draw
        assert self.V.keys() == self.P
        def tau(data_fiber):
            return restricted_tau.projection(data_fiber).values()
        mus = {'orientation': self.orientation}
        for (p, mu) in self.V.items():
            mus[p] = mu.nu(tau(mu.F))
        return mus
        
    @staticmethod
    def qhat(orientation, position, height, floor, width, facecolor, edgecolor, linewidth, linestyle):
        def make_bars(xval, xoff, yval, yoff):
            return [[(x, y), (x, y+yo), (x+xo, y+yo), (x+xo, y), (x, y)] 
            for (x, xo, y, yo) in zip(xval, xoff, yval, yoff)]

        if orientation == 'v':
            paths = make_bars(position, width, floor, height)
        else:
            paths = make_bars(floor, height, position, width)

        def fake_draw(render):
            for (p, fc, ec, lw, ls) in zip(paths, facecolor, edgecolor, linewidth, linestyle):
                gc = render.new_gc()
                gc.set_foreground(ec)
                gc.set_dashes(ls)
                gc.set_linewidth(lw)
                render.draw_path(gc, path, mtransforms.IdentityTransform(), fc)

        return fake_draw

class GenericArtist: #goes to add_artist
    def __init__(self, topArt):
        self.topArt = topArt

    def get_screen_bounds_to_data_bounds(self, renderer):
        """proxy for S->F over K"""
        # actual limits...scale...projections...
        # x1, x1
        return None

    def draw(self, renderer):
        # get bounding ax.get_xlim(), ax.get_ylim()
        # get bounding box from coordinates on screen to data coordinates
        # can compute 
        ### assume we have data bounds
        bounding_box = self.get_screen_bounds_to_data_bounds(renderer)
        tau_restricted = self.topArt.query(bounding_box)
        # you write make_mu & qhat so what gets passed into which
        mu = self.topArt.graphic.make_mu(tau_restricted)
        qhat = self.topArt.graphic.qhat(**mu)
        #rho = qhat(renderer)


#Q^(hat)(nu \circ (xi(axes_bound)=>tau))

#bind global bound, make make mu take in data bounds

# Xi
#* screen to fiber
#* fiber to k
# k to local sections