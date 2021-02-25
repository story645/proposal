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

    def assemble(self, x, y, s, facecolors='C0' ):
        # construct geometries of the circle glyphs in visual coordinates
        self._paths = [mpath.Path.circle(center=(xi,yi), radius=si) 
                       for (xi, yi, si) in zip(x, y, s)] 
        # set attributes of glyphs, these are vectorized 
        # circles and facecolors are lists of the same size
        self.set_facecolors(facecolors)
        
    def draw(self, renderer):
        # query data for a vertex table K
        view = self.data.view(self.axes) 
        visual = {p: t['encoder'](view[t['name']] 
                  if t['name'] in self.data.FB.F else t['name']) 
                  for p, t in self.transforms.items()}
        self.assemble(**visual)
        # call the renderer that will draw based on properties
        super().draw(renderer)