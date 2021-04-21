import copy
from collections import defaultdict
import itertools

import numpy as np 

from cycler import cycler

from matplotlib import rcParams
import matplotlib.collections as mcollections
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.artist as martist

from matplottoy.artists import utils



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