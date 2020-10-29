from collections import defaultdict
import itertools

import numpy as np 

from matplotlib import rcParams
import matplotlib.collections as mcollections
import matplotlib.path as mpath

import channels

class Point(mcollections.Collection):
    required = {'x', 'y'}
    optional = {'facecolors'} 
    def __init__(self, data, transforms, *args, **kwargs):
        """
        Parameters
        ----------
        data: sections of the fiber bundle
        transforms
        """
        super().__init__(*args, **kwargs)
        
        # check that the data you're trying to transform 
        # has a way to provide vertex data  
        assert 'vertex' in data.FB.K['tables']
        # check that you've given the required parameters
        assert Point.required <= transforms.keys()
        # this one might not be necessary 
        # (checks that rest of keys are valid)
        assert ((transforms.keys()-Point.required) 
                            <= Point.optional) 
        
        # checking that transform can take that type
        # group symmetry steo
        assert all(tau.validate(data.FB.F[column]) 
                    for (column, tau) in transforms.values())
        self.data = data
        self.transforms = transforms

    def draw(self, renderer, *args, **kwargs):
        view = self.data.view('vertex') #resolve to size

        # call tau step
        visual = dict([(t, tau.convert(view[var]))
            for (t, (var, tau)) in self.transforms.items()])
           
        # assembles taus to generate idiom
        # dictionary here in place of visual(parameter) function
        if 's' not in visual:
            visual['s'] = itertools.repeat(0.05)
        if 'facecolors' not in visual:
            visual['facecolors'] = "C0"
        #switch out to a marker 
        self._paths = [mpath.Path.circle(center=(x,y), radius=s)  
                        for (x, y, s) 
                        in zip(visual['x'],visual['y'], visual['s'])] 
       
        self.set_facecolors(visual['facecolors'])
        super().draw(renderer, *args, **kwargs)


class Line(mcollections.LineCollection):
    required = {'x', 'y'}
    optional = {'facecolor'} 
    def __init__(self, data, transforms, *args, **kwargs):
        """
        Parameters
        ----------
        data: sections of the fiber bundle
        transforms
        """
        super().__init__(None, *args, **kwargs)
        assert 'edge' in data.FB.K['tables']
        assert Line.required <= transforms.keys()
        assert ((transforms.keys()-Line.required) 
                            <= Line.optional) 
        assert all(tau.validate(data.FB.F[column]) 
                    for (column, tau) in transforms.values())
     
        self.data = data
        self.transforms = transforms

    def draw(self, renderer, *args, **kwargs):
      
        view = self.data.view('edge')
        visual = dict([(t, tau.convert(view[var]))
            for (t, (var, tau)) in self.transforms.items()])
           
        # dictionary here in place of visual(parameter) function
        if 'facecolor' not in visual:
            visual['facecolor'] = "C0"

        segments = [np.vstack((vx, vy)).T for vx, vy 
                    in zip(visual['x'], visual['y'])]

        self.set_segments(segments)
        self.set_color(visual['facecolor'])

        super().draw(renderer, *args, **kwargs)


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
        
        if 'floor' not in visual:
            visual['floor'] = itertools.repeat(0)
     
        if self.orientation in {'vertical', 'v'}:
            dims = {'x': 'position', 'xoffset': 'width', 
                    'y': 'floor',    'yoffset': 'length'}
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

    # going to back this into bar above 'cause shouldn't import channel
    transforms['floor'] = (floor, channels.Position())
    artists = []
    for group in transforms['groups']:
        transforms['length'] = group
        artists.append(Bar(data, transforms.copy(), orientation))
        transforms['floor'] += t[1](data.view()[t[0]])

    ax.add_artist(artists)
