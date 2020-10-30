from collections import defaultdict
import itertools

import numpy as np 

from matplotlib import rcParams
import matplotlib.collections as mcollections
import matplotlib.path as mpath

import channels

def _make_bars(xvalues, xoffsets, yvalues, yoffsets):
    return [[(x, y), (x, y+yo), (x+xo, y+yo), (x+xo, y), (x, y)] for 
            (x, xo, y, yo) in zip(xvalues, xoffsets, yvalues, yoffsets)]

class Bar(mcollections.Collection):
    required = {'position', 'length'}
    optional = {'width', 'floor', 'groups'}
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
        assert Bar.required <= transforms.keys()
        assert ((transforms.keys()-Bar.required) 
                            <= Bar.optional) 
        groups = transforms.pop("groups", [])
        print(transforms)
        assert all(tau.validate(data.FB.F[column]) 
                    for (column, tau) in transforms.values())
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
        
      
            visual['floor'] = itertools.repeat(0)
     
        if self.orientation in {'vertical', 'v'}:
            verts = _make_bars(visual['position'], visual['width'], 
                              visual['floor'], visual['length'])
        elif self.orientation in {'horizontal', 'h'}:
            verts = _make_bars(visual['floor'], visual['length'], 
                               visual['position'], visual['width'])

        self._paths = [mpath.Path(xy, closed=True) for xy in verts]
        self.set_edgecolors('k')
        super().draw(renderer, *args, **kwargs)
        return      


def stacked_bar(ax, data, transforms, orientation):
    floor = np.zeros(len(data.view()[transforms['position'][0]]))

    # this needs to be a class, can pull stuff from bar....
    # should not be putting stuff on data!
    data._view['floor'] = floor
    transforms['floor'] = ("floor", channels.Position())
    artists = []
    for group in transforms['groups']:
        transforms['length'] = group
        artists.append(Bar(data, transforms.copy(), orientation))
        transforms['floor'] += t[1](data.view()[t[0]])

    ax.add_artist(artists)
