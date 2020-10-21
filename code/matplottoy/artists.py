from collections import defaultdict
import itertools

from matplotlib import rcParams
import matplotlib.collections as mcollections
import matplotlib.path as mpath

def visual_transform(transform, key, data):
    measurements = map(transform[key]['section'], data)
    return map(transform[key]['encoding'], measurements)

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
        assert Point.required <= transforms.keys()
        assert ((transforms.keys()-Point.required) 
                            <= Point.optional) 
        assert all(tau.validate(data.F[column]) 
                    for (column, tau) in transforms.values())
        assert data.K['ndims'] == 0
        self.data = data
        self.transforms = transforms

    def draw(self, renderer, *args, **kwargs):
        view = self.data.view()

        visual = dict([(t, tau.convert(view[var]))
            for (t, (var, tau)) in self.transforms.items()])
           
        if 's' not in visual:
            visual['s'] = itertools.repeat(0.05)

        self._paths = [mpath.Path.circle(center=(x,y), radius=s)  
                        for (x, y, s) 
                        in zip(visual['x'],visual['y'], visual['s'])] 
       
        self.set_facecolors(visual['facecolors'])

        super().draw(renderer, *args, **kwargs)