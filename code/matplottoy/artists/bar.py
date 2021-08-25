from __future__ import annotations
from collections import namedtuple
import copy
from typing import Tuple, Optional


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
class Rho: # this is really rho = \qhat \circ \mu
    def mu(self, tau_restricted:dict):
        pass
    @staticmethod
    def qhat():
        pass

class TopologicalArtist: 
# also maybe should be owned by data library? 
#is bad name for this since this is more than just qhat
    def __init__(self, graphic:Rho):
        # is parameterized by the rho
        # only input is \tau (E)
        self.graphic = graphic
        self.data = None

    def compose_with_tau(self, section): #doesn't need to be there
        # do I care about bounds yet? or only at draw time?
        new = copy.copy(self)
        new.data = section
        return new

    def query(self, data_bounds:Optional[dict]=None, sampling_rate:Optional[int]=None)->dict:
        return self.data.query(data_bounds, sampling_rate)
        # section.view, #xi seperates nicely 

# BarH and BarV are different Q^{hat} so BarFactory returns the right Bar?
class Bar(RhoFactory): 
    #what are the 
    P = {'position', 'height', 'floor', 'width', 
         'facecolor', 'edgecolor', 'linewidth', 'linestyle'}
    
    def __init__(self, orientation='v', V:Optional[dict]=None):
        # F->V maps need to be fixed here, but use fiber name instead of function
        self.orientation = orientation
        self.V = {k:Mu(None,None) for k in self.P} if V is None else V

    # Spivak r: C \rightarrow U_{\sigma}, U_{sigma}=F_{i}=F_{c} 
    def compose_with_nu(self, pi:str, fi: Tuple[str,...], nu: callable)->Bar:
        #trying to sort out how to not lose existing specs
        # also maybe type checking here? (Is this nu valid for this fiber?)
        new = copy.copy(self)
        # user needs to do nu_i = nu_i_j \circ nu_i_k composition
        new.V[pi] = Mu(nu_i=nu, F_i=fi) 
        return new

    # yes argument this is a level up/ generates the mu
    @staticmethod
    def rename_P(V:dict, orientation:str)->dict:
        if orientation == 'v':
            new_key = {'position': 'x', 'height':'y'}
        elif orientation == 'h': 
            # needs to be a different artist 'cause data_bounds won't work here
            #data bounds need position y, height x
            new_key = {'floor':'x', 'height':'width', 
                       'width':'y', 'position':'floor'}
        return {(new_key[k] if k in new_key else k):v for (k, v) in V.items()}

    def mu(self, tau_restricted: dict)->dict: #draw
        V = self.rename_P(self.V, self.orientation)
        mus = {}
        mus['x'] = V['x'].nu_i(**(tau_restricted[f] for f in V['x'].F_i))
        mus['y'] = V['y'].nu_i(**(tau_restricted[f] for f in V['y'].F_i))
        V.pop('x')
        V.pop('y')

        for (p_i, mu_i) in V.items():
            if mu_i.F_i is None:
                pass
            else:
                mus[p_i] = mu_i.nu_i(*(tau_restricted[f] for f in mu_i.F_i)) 
       return mus
              

    @staticmethod
    def qhat(x, width, y, floor, facecolor, edgecolor, linewidth, linestyle):
        def fake_draw(render, transform=mtransforms.IdentityTransform()):
            for (xi, xw, yi, yf, fc, ec, lw, ls) in zip(x, width, y, floor, facecolor, edgecolor, linewidth, linestyle):
                gc = render.new_gc()
                gc.set_foreground((ec.r, ec.g, ec.b, ec.a))
                gc.set_dashes(*ls)
                gc.set_linewidth(lw)

                path = mpath.Path([(xi, yf), (xi, yf+yi), (xi+xw, yf+yi), 
                                  (xi+xw, yf),(xi, yf)], closed=True)
                render.draw_path(gc=gc, path=path, 
                    transform=transform, 
                    rgbFace=(fc.r, fc.g, fc.b, fc.a))
        return fake_draw


class GenericArtist(martist.Artist):
    # start w/ working w/ an artist object then stripped down artist
    def __init__(self, artist:TopologicalArtist):
        super().__init__()
        self.artist = artist
  
    def get_screen_bounds_to_data_bounds(self, renderer)->(dict, int):
        """proxy for S->F over K"""
        # actual limits...scale...projections...
        # x1, x1
        bbox = self.get_window_extent(renderer)

        return None, None

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
        for tau_restricted in self.artist.data.query(bounding_box, sampling_rate):
            # you write make_mu & qhat so what gets passed into which
            # \qhat \circ mu 
            mu = self.artist.graphic.mu(tau_restricted)
            rho = self.artist.graphic.qhat(**mu)
            H = rho(renderer, transform = self.axes.transData)