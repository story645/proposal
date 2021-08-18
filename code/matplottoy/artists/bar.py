import copy
from collections import defaultdict, namedtuple
from collections.abc import Iterable
from dataclasses import dataclass, field, asdict
import itertools
from typing import Iterable

import numpy as np 

from cycler import cycler

from matplotlib import rcParams

import matplotlib.artist as martist
import matplotlib.collections as mcollections
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.transforms as mtransforms

from matplottoy.artists import utils
from matplottoy.encoders import mtypes

class QHatData:
    def __init__(QHatWrapper, section):
        self.qhat_visual = QhatWrapper
        self.global_section = section
        pass

    def compose_with_tau(self, section): #doesn't need to be there
        # do I care about bounds yet? or only at draw time?
        new = copy.copy(self)
        new.section = section
        return new

    def query(self, data_bounds):
        return self.section.view(data_bounds)
        # section.view, #xi seperates nicely 


class QHatWrapper:
    def make_mu(self, bounds):
        pass
    @static
    def qhat():
        pass

class Bar(QhatWrapper): 
    # serializibiluty - you provide the exact same data, we give you the exact same thing
    # pull the data stuff out into another layer 
    def __init__(self):
        ### F->V maps need to be fixed here, but use fiber name instead of function
        # nu
        #Pi = Fi, nu_i
        self.position = None #(string, callable)
        self.height = None
        self.floor = None
        self.width = None
        self.facecolor = None
        self.edgecolor = None
        self.linewidth = None
        self.linestyle = None

    def compose_with_nu(self, **kwargs):
        #trying to sort out how to not lose existing specs
        # also maybe type checking here? (Is this nu valid for this fiber?)
        new = copy.copy(self) 
        for k, v in kwargs.items():
            setattr(new, k, v)    
        return new
        
    # curried mu then execute on restricted_tau 
    def make_mu(self, restricted_tau): #draw
        # curry all of this so it works w/o section?
        # projection(section, F1)
        # restricted_section.get
        # check if not none! 
        curred_mu_pos(restricted_tau)

        color \circ proj('fruit'

        position = nu_position()proj_(position_F, restricted_tau)
        self.position[1](xi(bounds)(position[0]))
        return position, height, floor, width, facecolor, edgecolor, linewidth, linestyle):
        
    @staticmethod
    def qhat(position, height, floor, width, facecolor, edgecolor, linewidth, linestyle):
        def make_bars(xval, xoff, yval, yoff):
            return [[(x, y), (x, y+yo), (x+xo, y+yo), (x+xo, y), (x, y)] 
            for (x, xo, y, yo) in zip(xval, xoff, yval, yoff)]

        path = make_bars()
        
        def fake_draw(render):
            renderer...
        return fake_draw()

class GenericQHatArtist(): #goes to add_artist)
    def __init__(self, QhatData):
        pass

    def get_screen_bounds_to_data_bounds(self, renderer):
        """proxy for S->F over K"""
        # actual limits...scale...projections...
        # x1, x1
        pass

    def draw(self, renderer):
        # get bounding ax.get_xlim(), ax.get_ylim()
        # get bounding box from coordinates on screen to data coordinates
        # can compute 
        ### assume we have data bounds
        bounding_box = self.get_screen_bounds_to_data_bounds(renderer)
        tau_restricted = self.QhatData.flobal_section.query(bounding_box)
        # you write make_mu & qhat so what gets passed into which
        mu = self.QhatData.qhat_visual.make_mu(tau_restricted)
        qhat = self.QhatData.qhat_visual.qhat(**mu)
        rho = qhat(renderer)


Q^(hat)(nu \circ (xi(axes_bound)=>tau))

#bind global bound, make make mu take in data bounds

# Xi
* screen to fiber
* fiber to k
* k to local sections