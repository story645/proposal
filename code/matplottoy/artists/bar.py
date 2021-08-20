from collections import namedtuple
import copy
from typing import Tuple


import numpy as np 

from matplotlib import rcParams


import matplotlib.artist as martist
import matplotlib.cbook as cbook
import matplotlib.path as mpath
import matplotlib.transforms as mtransforms

from matplottoy.artists import utils
from matplottoy.encoders import mtypes


# mu = \nu \circ \tau 
#\tau = data.query().projection()
Mu = namedtuple('Mu', ['nu_i', 'F_i'])


class QHatData: 
# also maybe should be owned by data library? 
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
        return self.section.query(data_bounds)
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
        self.V = {k:Mu(None,None) for k in self.P} if V is None else V
\
        
    def compose_with_nu(self, pi:str, fi: Tuple[str,...], nu: callable, ):
        #trying to sort out how to not lose existing specs
        # also maybe type checking here? (Is this nu valid for this fiber?)
        new = copy.copy(self)
        new.V[pi] = Mu(nu=nu, fi=fi)
        return new

    def make_mu(self, restricted_tau): #draw
        assert self.V.keys() == self.P

        mus = {'orientation': self.orientation}
        tau_restricted = {'fiber', tau_f()}
        # mu = nu \circ \tau
        # {P_i: numpy Arry} = nu ({F_i: [numpy_array]_{u_j}?})
        # fiber_bundle is on matching the {u_j}, condition
        # nu({F_i: [f1, f2, f3]}) # [{F_i: f1}, {F_i:f2}]
        # F_i is a tuple 
        # nu({(F_i, F_2): [f11, f21]} )  

        mus = []
        for tau in tau_restricted: #pull out to other draw method
            for (p_i, mu_i) in self.V.items():
                # this is where we're realizing the data
                # mus[p_i] = mu_i.nu_i(tau(mu_i.F_i))
                # loop over tau restricted for each F 
                mus[p_i] = mu_i.nu_i(*(tau_restricted[f] for f in mu_i.F_i))

        return mus #either returns V or spec of V
        
    @staticmethod
    def qhat(orientation, position, height, floor, width, facecolor, edgecolor, linewidth, linestyle):
        def make_bars(xval, xoff, yval, yoff):
            return [mpath.Path([(x, y), (x, y+yo), (x+xo, y+yo), (x+xo, y), (x, y)]) 
            for (x, xo, y, yo) in zip(xval, xoff, yval, yoff)]

        if orientation == 'v':
            paths = make_bars(position, width, floor, height)
        else:
            paths = make_bars(floor, height, position, width)

        def fake_draw(render):
            for (p, fc, ec, lw, ls) in zip(paths, facecolor, edgecolor, linewidth, linestyle):
                gc = render.new_gc()
                gc.set_foreground(ec)
                gc.set_dashes(*ls)
                gc.set_linewidth(lw)
                print(p)
                render.draw_path(gc=gc, path=p, transform=mtransforms.IdentityTransform(), rgbFace=fc)
        return fake_draw


class GenericArtist(martist.Artist):
    # start w/ working w/ an artist object then stripped down artist
    def __init__(self, topArt):
        super().__init__()
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
        # part of Xi -> converts screen to data
        bounding_box, sampling_rate = self.get_screen_bounds_to_data_bounds(renderer)
        # tau: U\subset K \rightarrow F
        #topArtist.graphic.V.items()[0]
        
        # maybe do loop over taus here (local section of taus)
        for tau_restricted in self.topArt.query(bounding_box, sampling_rate):
            # you write make_mu & qhat so what gets passed into which
            # \qhat \circ mu 
            mus = self.topArt.graphic.make_mu(tau_restricted)
            for mu in mus: #is a ufunc
                qhat = self.topArt.graphic.qhat(**mu)
            rho = qhat(renderer)


#Q^(hat)(nu \circ (xi(axes_bound)=>tau))

#bind global bound, make make mu take in data bounds

# Xi
#* screen to fiber
#* fiber to k
# k to local sections