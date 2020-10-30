from collections import defaultdict
import itertools

import numpy as np 

from matplotlib import rcParams
import matplotlib.collections as mcollections
import matplotlib.path as mpath

import channels

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