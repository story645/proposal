from collections import defaultdict
import itertools

import numpy as np 

from matplotlib import rcParams
import matplotlib.collections as mcollections
import matplotlib.path as mpath

from matplottoy.artists import utils

def _make_bars(orientation, position, width, floor, length):
    if orientation in {'vertical', 'v'}:
        xval, xoff, yval, yoff = position, width, floor, length
    elif orientation in {'horizontal', 'h'}:
        xval, xoff, yval, yoff = floor, length, position, width
    return [[(x, y), (x, y+yo), (x+xo, y+yo), (x+xo, y), (x, y)] 
            for (x, xo, y, yo) in zip(xval, xoff, yval, yoff)]

class Bar(mcollections.Collection):
    required = {'position', 'length'}
    optional = {'width', 'floor'}
    def __init__(self, data, transforms, *args, **kwargs):
        """
        Parameters
        ----------
        datasource: matplottoy.datasources.DataSource like
            data object containing data to be plotted
        stacked: bool, optional
            True: bar chart is stacked (groups are added)
            False: bar chart is unstacked (groups are interspersed)
        orientation: str, optional
            vertical: bars aligned along x axis, heights on y
            horizontal: bars aligned along y axis, heights on x
        **kwargs:
            kwargs passed through 
        """
  
        assert 'vertex' in data.FB.K['tables']
        utils.check_constraints(Bar, transforms)
        assert utils.validate_transforms(data, transforms)

        self.orientation = kwargs.pop('orientation', 'v')
     
        super().__init__(*args, **kwargs)
        self.data = data
        self.transforms = transforms

        
    
    def draw(self, renderer, *args, **kwargs):
       
        view = self.data.view('vertex')
        visual = dict([(t, tau.convert(view[var]))
            for (t, (var, tau)) in self.transforms.items()])
        
        if 'width' not in visual:
            visual['width'] = itertools.repeat(0.8)
        
        if 'floor' not in visual:
            visual['floor'] = itertools.repeat(0)
     
        verts = _make_bars(self.orientation, visual['position'], 
                   visual['width'], visual['floor'], visual['length'])

        self._paths = [mpath.Path(xy, closed=True) for xy in verts]
        self.set_edgecolors('k')
        super().draw(renderer, *args, **kwargs)
        return      

class MultiBar(mcollections.Collection):
    required = {'position', 'length'}
    optional = {'width', 'floor'}
    def __init__(self, data, transforms, *args, **kwargs):
        """
        Parameters
        ----------
        datasource: matplottoy.datasources.DataSource like
            data object containing data to be plotted
        stacked: bool, optional
            True: bar chart is stacked (groups are added)
            False: bar chart is unstacked (groups are interspersed)
        orientation: str, optional
            vertical: bars aligned along x axis, heights on y
            horizontal: bars aligned along y axis, heights on x
        **kwargs:
            kwargs passed through         """
  
        assert 'vertex' in data.FB.K['tables']
        self.transforms = transforms.copy()
        utils.check_constraints(MultiBar, self.transforms)
        length = self.transforms.pop('length') # allowed to be >1
        assert utils.validate_transforms(data, self.transforms)
        assert utils.validate_columns(data, length[0], length[-1])

        self.orientation = kwargs.pop('orientation', 'v')
        self.stacked = kwargs.pop('stacked', False)     
        self.width = kwargs.pop('width', .8)
        super().__init__(*args, **kwargs)
        self.data = data
        self.groups = length

    def draw(self, renderer, *args, **kwargs):
       
        view = self.data.view('vertex')
        visual = dict([(t, tau.convert(view[var]))
            for (t, (var, tau)) in self.transforms.items()])

        nitems = len(view[self.groups[0]])
        ngroups = len(np.atleast_1d(length[0]))

        if 'floor' not in visual: 
            visual['floor'] = np.empty(nitems)
     
        if 'width' not in visual and self.stacked:
            visual['width'] = itertools.repeat(self.width)
        elif 'width' not in visual and not self.stacked:
            visual['width'] = self.width/ngroups
            offset = np.arange(nitems)/nitems
       
        verts = []
        for group in self.groups:
            visual['length'] = view[group]
            verts = _make_bars(self.orientation, visual['position'], 
                     visual['width'], visual['floor'], visual['length'])
            if stacked:
                visual['floor'] += visual['length']

            verts.extend(_make_bars(self.orientation, visual['position'], 
                         visual['width'], visual['floor'], visual['length']))
        #convert paths after all calculations are made
        self._paths = [mpath.Path(xy, closed=True) for xy in verts]
        self.set_edgecolors('k')
        super().draw(renderer, *args, **kwargs)
        return      

