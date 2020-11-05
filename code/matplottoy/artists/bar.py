from collections import defaultdict
import itertools

import numpy as np 

from cycler import cycler

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
    optional = {'width', 'floor', 'color'}
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
        utils.validate_transforms(data, transforms)

        self.orientation = kwargs.pop('orientation', 'v')
     
        super().__init__(*args, **kwargs)
        self.data = data
        self.transforms = transforms

        
    
    def draw(self, renderer, *args, **kwargs):
       
        view = self.data.view('vertex')
        visual = utils.convert_transforms(view, self.transforms)  
        
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
    optional = {'width', 'floor', 'color'}
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
        utils.check_constraints(MultiBar, transforms)
        utils.validate_transforms(data, transforms)
       

        self.orientation = kwargs.pop('orientation', 'v')
        self.stacked = kwargs.pop('stacked', False)     
        self.width = kwargs.pop('width', .8)
       
        super().__init__(*args, **kwargs)
        self.data = data
        self.transforms = transforms.copy()

    def draw(self, renderer, *args, **kwargs):
       
        view = self.data.view('vertex')
        (groups, gtau) = self.transforms['length']
        ngroups = len(np.atleast_1d(groups))

        visual = utils.convert_transforms(view, self.transforms, ['length'])   

        if 'floor' not in visual: 
            visual['floor'] = np.empty(len(view[groups[0]]))

        if 'width' not in visual and self.stacked:
            visual['width'] = itertools.repeat(self.width)

        if not self.stacked:
            visual['width'] = itertools.repeat(self.width/ngroups)
            offset = (np.arange(ngroups) /ngroups) * self.width
        else:
            offset = itertools.repeat(0)

        if 'color' not in visual:
            visual['color'] = 'C0'

        verts = []
        for group, off in zip(groups, offset):
            verts.extend(_make_bars(self.orientation, visual['position'] + off, 
                          visual['width'], visual['floor'], view[group]))
            if self.stacked:
                visual['floor'] += view[group]
          

        # convert lengths after all calculations are made
        # here or in transform machinery?
        if self.orientation in {'v', 'vertical'}:
            tverts = [[(x, gtau.convert(y)) for (x, y) in vert] 
                            for vert in verts]
        elif self.orientation in {'h', 'horizontal'}:
            tverts = [[(gtau.convert(x), y) for (x, y) in vert] 
                            for vert in verts]
        self._paths = [mpath.Path(xy, closed=True) for xy in tverts]

        self.set_facecolor(list(itertools.chain.from_iterable(visual['color'])))
        self.set_edgecolors('k')
        super().draw(renderer, *args, **kwargs)
        return      

