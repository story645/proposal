from collections import defaultdict
import itertools

import numpy as np 

from matplotlib import rcParams
import matplotlib.collections as mcollections
import matplotlib.path as mpath


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
        assert data.K['ndims'] == 0
        assert Point.required <= transforms.keys()
        assert ((transforms.keys()-Point.required) 
                            <= Point.optional) 
        assert all(tau.validate(data.F[column]) 
                    for (column, tau) in transforms.values())
        self.data = data
        self.transforms = transforms

    def draw(self, renderer, *args, **kwargs):
        view = self.data.view()

        visual = dict([(t, tau.convert(view[var]))
            for (t, (var, tau)) in self.transforms.items()])
           
        # dictionary here in place of visual(parameter) function
        if 's' not in visual:
            visual['s'] = itertools.repeat(0.05)
        if 'facecolors' not in visual:
            visual['facecolors'] = itertools.repeat("black")

        self._paths = [mpath.Path.circle(center=(x,y), radius=s)  
                        for (x, y, s) 
                        in zip(visual['x'],visual['y'], visual['s'])] 
       
        self.set_facecolors(visual['facecolors'])
        super().draw(renderer, *args, **kwargs)


class Line(mcollections.LineCollection):
    required = {'y'}
    optional = {'x', 'color'} 
    def __init__(self, data, transforms, *args, **kwargs):
        """
        Parameters
        ----------
        data: sections of the fiber bundle
        transforms
        """
        super().__init__(None, *args, **kwargs)
        assert data.K['ndims'] == 1

        assert Line.required <= transforms.keys()
        assert ((transforms.keys()-Line.required) 
                            <= Line.optional) 
        assert all(tau.validate(data.F[column]) 
                    for (column, tau) in transforms.values())
     
        self.data = data
        self.transforms = transforms

    def draw(self, renderer, *args, **kwargs):
        view = self.data.view()

        visual = dict([(t, tau.convert(view[var]))
            for (t, (var, tau)) in self.transforms.items()])
           
        # dictionary here in place of visual(parameter) function
        if 'color' not in visual:
            visual['color'] = "C0"

        if 'x' in visual:
            segments = [np.vstack((visual['x'], visual['y'])).T]
        else:
            # if an x is not given, than the y transform needs to also yield an x
            segments = []
        self.set_segments(segments)
        self.set_color(visual['color'])

        super().draw(renderer, *args, **kwargs)