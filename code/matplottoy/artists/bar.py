import copy
from collections import defaultdict
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


class BarArtist(martist.Artist):
    def __init__(self, orientation, aes, position, length, floor, width, facecolor, edgecolor, linewidth, linestyle):
        """
        Parameters
        ----------
        dictionary specifying which columns of the data are bound to which columns?
            # maybe bake this into the tau instead
        position (callable, [component names])
        # position, length,..... pass in callables
        aes: [{'data': data components, 'aes': visual components}]
            dictionary specifying which columns of the data are bound to which columns?
                # maybe bake this into the tau instead
        
        orientation: str
            vertical: bars aligned along x axis, heights on y
            horizontal: bars aligned along y axis, heights on x
        **kwargs:
            kwargs passed through 
        """

        self.orientation = orientation
        # the nu functions are attributes of a fully specified artist
        
        self.aes = aes.copy()
        # maybe this should just be verical/horizontal wrapper functions/Artists  
        if self.orientation in {'vertical', 'v'}:
            self.aes.update({new_key: self.aes.pop(old_key) 
                        for old_key, new_key in 
                        {'position':'x0', 'width':'x1', 
                         'floor':'y0', 'length':'y1'}})
            self._x0 = position
            self._x1 = width
            self._y0 = floor
            self._y1 = length
        elif self.orientation in {'horizontal', 'h'}:
            self.aes.update({new_key: self.aes.pop(old_key) 
                        for old_key, new_key in 
                        {'floor':'x0', 'length':'x1',
                         'position':'y1', 'width':'y1'}})
            self._x0 = floor
            self._x1 = length
            self._y0 = position
            self._y1 = width

        self._facecolors = facecolors
        self._edgecolors = edgecolors
        self._linewidths = linewidths
        self._linestyles = linestyles
        
        super().__init__()
        
    
    def __call__(data):
        #BarArtist(data.view())
        # do we want to freeze the data at call time or draw time? 
        self.view = data.view(self.axes) 
        #place where data is subsetted/prepped - this is setting up the sheaf rules, not pulling the data over yet, that's a seperate get? method
        #rewrite the view object as a generator? 
        #pass info about axes -> that's where do subsampling into data
        #can't be here? needs the axes -> actually can also happen in 
        # this allows for Artist(Data) where A = q\circ nu & xi
              #current limits, downsampling, etc ()
        # calling xi to get range, passing range to them
        # from limits on axes/scales, resample
        # how to filter to an xrange is dstructure depenedent
        # bounds based on inverses of nu....
        
        # should maybe return something that isn't executed yet
        # batch()

        # passing axes back is an optimization
        # tau is sinx -> in assembly sinx(axes)

        #k-based indexing on rows
        # nu needs to be applied at draw time so mu can be dynamically updated on draw
        return self

    #maybe pull this out so it's reusable (make it purely functional):
    @staticmethod
    def make_bars(xval, xoff, yval, yoff):
        return [[(x, y), (x, y+yo), (x+xo, y+yo), (x+xo, y), (x, y)] 
                for (x, xo, y, yo) in zip(xval, xoff, yval, yoff)]
        
    #this is to debug encodings in V seperate from rendering, 
    # is also what gets realized - this can also be the callable....
    def assemble(self):
        #do promotion in the get 
        paths = [mpath.Path([(x0, y0), (x0, y0+y1), 
                             (x0+x1, y0+y1), (x0+x1, y0)], closed=True)   
                 for (x0, x1, y0, y1) 
                 in zip (self._x0(self.view.get(self.aes['x0'])),
                         self._x1(self.view.get(self.aes['x1'])), 
                         self._y0(self.view.get(self.aes['y0'])), 
                         self._y1(self.view.get(self.aes['y1'])))]
            
        facecolors = self._edgecolor(self.view.get(self.aes['facecolor']))
        edgecolors = self._edgecolor(self.view.get(self.aes['edgecolor']))
        linewidths = self._linewidth(self.view.get(self.aes['linewidth']))
        linestyles = self._linestyle(self.view.get(self.aes['linestyle']))
        
        transforms = np.repeat(mtransforms.IdentityTransform(),   self.view.N)
        offsets = np.zeros(self.view.N)
        offsetTrans = np.repeat(mtransforms.IdentityTransform(), self.view.N)
        antialiaseds = np.repeat(True, self.view.N)
        urls = np.repeat(True, self.view.N)
        offset_position = 'screen'
        # this validates that nu outputs the correct types
        return DrawPathCollection(paths, transforms, offsets, facecolors, edgecolors, linewidths, linestyles, antialiaseds, urls, offset_position)
        
    def draw(self, renderer,  *args, **kwargs): #actually 
        spec = self.assemble() # in assemble is where nu \circ tau, and assembled into graphical design
        #gc = renderer.new_gc()
        #renderer.draw_path_collection(gc, master_transform=mtransforms.IdentityTransform(),)
        #super().draw(renderer,  *args, **kwargs)


class Bar(mcollections.Collection):
    def __init__(self, data, transforms, orientation='v', *args, **kwargs):
        """
        Parameters
        ----------
        datasource: matplottoy.datasources.DataSource like
            data object containing data to be plotted
        orientation: str, optional
            vertical: bars aligned along x axis, heights on y
            horizontal: bars aligned along y axis, heights on x
        **kwargs:
            kwargs passed through 
        """
  
        #assert 'vertex' in data.FB.K['tables']
        #utils.check_constraints(Bar, transforms)
        #utils.validate_transforms(data, transforms)

        self.orientation = orientation
     
        super().__init__(*args, **kwargs)
        self.data = data
        self.transforms = copy.deepcopy(transforms)
    
    def assemble(self, position, length, floor=0, width=0.8, facecolors='C0', edgecolors='k', offset=0):
        #set some defaults
        width = itertools.repeat(width) if np.isscalar(width) else width
        floor = itertools.repeat(floor) if np.isscalar(floor) else (floor)
        
        # offset is passed through via assemblers such as multigroup, not supposed to be directly tagged to position 
        position = position + offset
        
        def make_bars(xval, xoff, yval, yoff):
             return [[(x, y), (x, y+yo), (x+xo, y+yo), (x+xo, y), (x, y)] 
                for (x, xo, y, yo) in zip(xval, xoff, yval, yoff)]
        #build bar glyphs based on graphic parameter
        if self.orientation in {'vertical', 'v'}:
            verts = make_bars(position, width, floor, length)
        elif self.orientation in {'horizontal', 'h'}:
            verts = make_bars(floor, length, position, width)
        
        self._paths = [mpath.Path(xy, closed=True) for xy in verts]
        self.set_edgecolors(edgecolors)
        self.set_facecolors(facecolors)
        
    def draw(self, renderer,  *args, **kwargs):
        view = self.data.view(self.axes)
        visual = {}
        for (p, t) in self.transforms.items():
            if isinstance(t, dict):
                if t['name'] in self.data.FB.F and 'encoder' in t:
                    visual[p] = t['encoder'](view[t['name']])
                elif 'encoder' in t:
                    visual[p] = t['encoder'](t['name'])
                elif t['name'] in self.data.FB.F:
                    visual[p] = view[t['name']]
            else:
                 visual[p] = t
        self.assemble(**visual)
        super().draw(renderer,  *args, **kwargs)

class StackedBar(martist.Artist):
    def __init__(self, data, transforms, mtransforms, orientation='v', *args, **kwargs):
        """
        Parameters
        ----------
   
        orientation: str, optional
            vertical: bars aligned along x axis, heights on y
            horizontal: bars aligned along y axis, heights on x   
        """
        super().__init__(*args, **kwargs)
        self.data = data
        self.orientation = orientation
        self.transforms = copy.deepcopy(transforms)
        self.mtransforms = copy.deepcopy(mtransforms)

    def assemble(self):
        view = self.data.view(self.axes)
        self.children = [] # list of bars to be rendered
        floor = 0
  
        for group in self.mtransforms:
            # pull out the specific group transforms
            bar = Bar(self.data, {**group, **self.transforms, 'floor':floor}, self.orientation, transform=self.axes.transData)
            self.children.append(bar)
            floor += view[group['length']['name']]
            
            
    def draw(self, renderer, *args, **kwargs):

        # all the visual conversion gets pushed to child artists
        self.assemble()
        #self._transform = self.children[0].get_transform()
        for artist in self.children:
            artist.draw(renderer, *args, **kwargs)

            
class GroupedBar(martist.Artist):
    def __init__(self, data, transforms, mtransforms, orientation='v', *args, **kwargs):
        """
        Parameters
        ----------
        orientation: str, optional
            vertical: bars aligned along x axis, heights on y
            horizontal: bars aligned along y axis, heights on x   
        """
        super().__init__(*args, **kwargs)
        self.data = data
        self.orientation = orientation
        self.transforms = copy.deepcopy(transforms)
        self.mtransforms = copy.deepcopy(mtransforms)

    def assemble(self):
        self.children = [] # list of bars to be rendered
        ngroups = len(self.mtransforms)
        
        for gid, group in enumerate(self.mtransforms):
            group.update(self.transforms)
            width = group.get('width',.8)
            gwidth = width/ngroups
            offset = gid/ngroups*width 
            bar = Bar(self.data, {**group, **self.transforms,'width':gwidth, 'offset':offset},
                        self.orientation, transform=self.axes.transData)     
            self.children.append(bar)
            
            
    def draw(self, renderer, *args, **kwargs):
        view = self.data.view(self.axes)
        # all the visual conversion gets pushed to child artists
        self.assemble()
        #self._transform = self.children[0].get_transform()
        for artist in self.children:
            artist.draw(renderer, *args, **kwargs)