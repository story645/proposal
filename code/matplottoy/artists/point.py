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
        super().__init__(*args, **kwargs)
        
        # check that the data you're trying to transform 
        # has a way to provide vertex data  
        assert 'vertex' in data.FB.K['tables']
        # check that you've given the required parameters
        utils.check_constraints(Point, transforms.keys())
        utils.validate_transforms(data.FB.F, transforms)

        self.data = data
        self.transforms = transforms

    def draw(self, renderer, *args, **kwargs):
        view = self.data.view('vertex') #resolve to size

        # call tau step
        visual = utils.convert_transforms(view, self.transforms)
           
        # assembles taus to generate idiom
        # dictionary here in place of visual(parameter) function
       
        visual['s'] = itertools.repeat(visual.get('s', 0.05))
        visual['facecolors'] = visual.get('facecolors', "C0")
        #switch out to a marker 
        self._paths = [mpath.Path.circle(center=(x,y), radius=s)  
                        for (x, y, s) 
                        in zip(visual['x'],visual['y'], visual['s'])] 
       
        self.set_facecolors(visual['facecolors'])
        super().draw(renderer, *args, **kwargs)