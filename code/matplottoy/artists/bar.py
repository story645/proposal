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
        self.transforms = transforms
    
    def assemble(self, visual):
        #set some defaults
        visual.setdefault('width', itertools.repeat(0.8))
        visual.setdefault('floor', itertools.repeat(0))
        visual.setdefault('facecolors', 'C0')
        #build bar glyphs based on graphic parameter
        if self.orientation in {'vertical', 'v'}:
            order = ['position', 'width', 'floor', 'length']
        elif self.orientation in {'horizontal', 'h'}:
            order = ['floor', 'length', 'position', 'width']
        
        verts = [[(x, y), (x, y+yo), (x+xo, y+yo), (x+xo, y), (x, y)] 
                for (x, xo, y, yo) in zip(*[visual[k] for k in order])]
        self._paths = [mpath.Path(xy, closed=True) for xy in verts]
        self.set_edgecolors('k')
        self.set_facecolors(visual['facecolors'])
        
    def draw(self, renderer):
        view = self.data.view(self.axes)
        visual = {p: encoder(view[f] if f is not None else None) 
                  for p, (f, encoder) in self.transforms.items()}
        self.assemble(visual)
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
        assert ('length' in mtransforms) # this is the criteria for stacked bar

    def assemble(self, view):
        self.children = [] # list of bars to be rendered
        ngroups = len(self.mtransforms['length'][0])
        gtransforms = self.transforms.copy()
        floor = 0
        for gid in range(ngroups):    
            # pull out the specific group transforms
            gtransforms['floor'] = (None, lambda _ : floor)
            gtransforms.update({k: (group[gid], encoder) for 
                    (k, (group, encoder)) in self.mtransforms.items()})
            bar = Bar(self.data, gtransforms, self.orientation)
            self.children.append(bar)
            (key, encoder) = self.mtransforms['length']
            floor += encoder(view[key])
      
    
    def draw(self, renderer):
        view = self.data.view(self.axes)
        # all the visual conversion gets pushed to child artists
        children = self.assemble(view)
        for artist in self.children:
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

