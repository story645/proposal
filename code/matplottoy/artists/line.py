from collections import defaultdict
import itertools

import numpy as np 

from matplotlib import rcParams
import matplotlib.collections as mcollections
import matplotlib.path as mpath

from matplottoy.artists import utils

## should probably remove transforms and spell out *args, **kwargs?
class Line(mcollections.LineCollection):
    required = {'x', 'y'}
    optional = {'color'} 
    def __init__(self, data, transforms, *args, **kwargs):
        """
        Parameters
        ----------
        data: sections of the fiber bundle
        transforms
        """
        super().__init__(None, *args, **kwargs)
        #assert 'edge' in data.FB.K['tables']
        #utils.check_constraints(Line, transforms)
        #utils.validate_transforms(data.FB.F, transforms)
     
        self.data = data
        self.transforms = transforms

    def assemble(self, x, y, color='C0'):
        #assemble line marks as set of segments 
        segments = [np.vstack((vx, vy)).T for vx, vy 
                    in zip(x, y)]
        self.set_segments(segments)
        self.set_color(color)
        
    def draw(self, renderer):
        # query data source for edge table
        view = self.data.view('edge')
        visual = {p: encoder(view[f] if f in self.data.FB.F else f) 
                     for p, (f, encoder) in self.transforms.items()}
        self.assemble(**visual)
        super().draw(renderer)

