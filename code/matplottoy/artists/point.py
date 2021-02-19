from collections import defaultdict
import itertools

import numpy as np 

from matplotlib import rcParams
import matplotlib.collections as mcollections
import matplotlib.path as mpath

from matplottoy.artists import utils

class Point(mcollections.Collection):
    # this is the visual fiber 
    required = {'x', 'y'}
    optional = {'facecolors', 's'} 
    def __init__(self, data, transforms, *args, **kwargs):
        """
        Parameters
        ----------
        data: sections of the fiber bundle
        transforms
        """
        # check that the data you're trying to transform 
        # has a way to provide vertex data  
        # assert 'vertex' in data.FB.K['tables']
        # check that you've given the required parameters
        #utils.check_constraints(Point, transforms.keys())
        #utils.validate_transforms(data.FB.F, transforms)
        super().__init__(*args, **kwargs)
        self.data = data
        self.transforms = transforms

    def assemble(self, visual):
        # construct geometries of the circle glyphs in visual coordinates
        self._paths = [mpath.Path.circle(center=(x,y), radius=s) for (x, y, s) 
                in zip(visual['x'],visual['y'], visual['s'])] 
        # set attributes of glyphs, these are vectorized 
        # circles and facecolors are lists of the same size
        self.set_facecolors(visual['facecolors'])
        
    def draw(self, renderer, *args, **kwargs):
        # query data for a vertex table K
        view = self.data.view(self.axes) 
        visual = {p: encoder(view[f] if f is not None else None) for p, (f, encoder) in self.transforms.items()}
        self.assemble(visual)
        # call the renderer that will draw based on properties
        super().draw(renderer, *args, **kwargs)