from matplotlib import rcParams
import matplotlib.collections as mcollections
import matplotlib.path as mpath

def visual_transform(transform, key, data):
    measurements = map(transform[key]['section'], data)
    return map(transform[key]['encoding'], measurements)

class Point(mcollections.Collection):
    required = {'x', 'y'}
    optional = {'color'} 
    def __init__(self, data, transforms):
        """
        Parameters
        ----------
        data: sections of the fiber bundle
        transforms
        """
        assert Point.required <= transforms.keys()
        self.optional_encodings = (transforms.keys()-Point.required)
        self.data = data
        self.transforms = transforms

     def draw(self, renderer, *args, **kwargs):
         x = visual_transform(self.transforms, 'x', self.data)
         y = visual_transform(self.transforms, 'y', self.data)

         color = visual_transform(self.transforms, 'color', self.data)
         
         for (x, y, r) in zips):
            paths.append(c)

      
        self.__draw(renderer, *args, **kwargs)
