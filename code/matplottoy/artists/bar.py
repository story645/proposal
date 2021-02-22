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
        self.transforms = transforms.copy()
    
    def assemble(self, position, length, floor=0, width=0.8, facecolors='C0', edgecolors='k'):
        #set some defaults
        width = itertools.repeat(width) if np.isscalar(width) else width
        floor = itertools.repeat(floor) if np.isscalar(floor) else (floor)
        
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
        
    def draw(self, renderer):
        view = self.data.view(self.axes)
        visual = {}
        for (p, trans) in self.transforms.items():
            if 'encoder' in trans:
                visual[p] = trans['encoder'](view[trans['name']])
            elif 'name' in trans:
                visual[p] = view[trans['name']]
            else:
                visual[p] = trans                              
                                                
        self.assemble(**visual)
        super().draw(renderer)

class StackedBar(martist.Artist):
    def __init__(self, data, transforms, mtransforms, orientation='v', *args, **kwargs):
        """
        Parameters
        ----------
   
        orientation: str, optional
            vertical: bars aligned along x axis, heights on y
            horizontal: bars aligned along y axis, heights on x
        **kwargs:
            kwargs passed through         
        """

       
        super().__init__(*args, **kwargs)
        self.data = data
        self.orientation = orientation
        self.transforms = transforms.copy()
        self.mtransforms = mtransforms.copy()

    def assemble(self, view):
        self.children = [] # list of bars to be rendered
        floor = np.zeros(len(view[self.transforms['position']['name']]))      
        for group in self.mtransforms:
            # pull out the specific group transforms
            gtransforms = self.transforms.copy()
            gtransforms.update(group)
            gtransforms['floor'] = floor
            bar = Bar(self.data, gtransforms, self.orientation)
            self.children.append(bar)
            floor += view[group['length']['name']]
            
            
    def draw(self, renderer):
        view = self.data.view(self.axes)
        # all the visual conversion gets pushed to child artists
        self.assemble(view)
        for artist in self.children:
            print("DRAW")
            artist.draw(renderer)

        
class MultiBar(mcollections.Collection):
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
  
        #assert 'vertex' in data.FB.K['tables']
        #utils.check_constraints(MultiBar, transforms)
        #utils.validate_transforms(data, transforms)
       

        self.orientation = kwargs.pop('orientation', 'v')
        self.stacked = kwargs.pop('stacked', False)     
        self.width = kwargs.pop('width', .8)
       
        super().__init__(*args, **kwargs)
        self.data = data
        self.transforms = transforms.copy()

    def assemble(self, visual, view):
        (groups, gencoder) = self.transforms['length']
        ngroups = len(np.atleast_1d(groups))
        visual['floor'] = visual.get('floor', np.empty(len(view[groups[0]])))
        visual['facecolors'] = visual.get('facecolors', 'C0')
        if 'width' not in visual and self.stacked:
            visual['width'] = itertools.repeat(self.width)

        if not self.stacked:
            visual['width'] = itertools.repeat(self.width/ngroups)
            offset = (np.arange(ngroups) /ngroups) * self.width
        else:
            offset = itertools.repeat(0)

        verts = []
        for group, off in zip(groups, offset):
            Bar(self.data, self.transforms)
            verts.extend(Bar._make_bars(self.orientation, visual['position'] + off, 
                          visual['width'], visual['floor'], view[group]))
            if self.stacked:
                visual['floor'] += view[group]
          
        # convert lengths after all calculations are made
        # here or in transform machinery?
        if self.orientation in {'v', 'vertical'}:
            tverts = [[(x, gencoder(y)) for (x, y) in vert] 
                            for vert in verts]
        elif self.orientation in {'h', 'horizontal'}:
            tverts = [[(gencoder(x), y) for (x, y) in vert] 
                            for vert in verts]
        self._paths = [mpath.Path(xy, closed=True) for xy in tverts]

        self.set_facecolor(list(itertools.chain.from_iterable(visual['facecolors'])))
        self.set_edgecolors('k')
        
        
        
    def draw(self, renderer, *args, **kwargs):
        view = self.data.view('vertex')
        #exclude converting the group visual length, special cased in assemble
        visual = utils.convert_transforms(view, self.transforms, ['length'])
        # pass in view because there's a visual conversion step that 
        # may need to happen after the glyphs ar put together
        self.assemble(visual, view)
        
        super().draw(renderer, *args, **kwargs)
        return      

