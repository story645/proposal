from types import SimpleNamespace
import numpy as np 

import matplotlib.image as mimage
import matplotlib.collections as mcollections

# datasource maps D->Projection for artist (query)
# aesthetic maps P-> retinal variables (red, sqaure)
# artist maps retinal variables -> pixels (CW-complex)

# axis should own view limits, 
# artist should own bounds
# scatter-parasite histograms 

# for Dashboards, they need to pass in a datasource object

def user_plotting_method(data):
    # user a .describe instead of is instance...
    if not isinstance(data, DataSource):
        datasource= DataSource(data) # goes through registry
    
class DataSource: #set of classes replaces _preprocess_data
    # documents interface 
    pass 
    
class DataSourceDict(DataSource):
    pass # assume this is like a dataframe, labels = columns
class DataSourceDictView(DataSource):
    pass
class Enums(DataSource):
    # name, value pair where value can contain multiples
    pass

class DataSourceArray(DataSource):
    def __init__(self, arr):
        self.data = arr
        
    def projectArray(self, ax, *args):
        data = self.data
        #.5 so 0,0 is at center of pixel
        extent = [-.5, data.shape[1]-.5, -.5, data.shape[0]-.5]
        return SimpleNamespace(data=data, extent=extent)
    
    def projectLine2D(self, ax, *args):
        data = [np.array((np.arange(len(y)), y)).T for y in self.data.T]   
        return SimpleNamespace(data=data)

class ArrayImage(mimage.AxesImage):
    def __init__(self, ax, datasource, *args, **kwargs):
        super().__init__(ax, *args, **kwargs)
        self.DataSource = datasource
        
    def draw(self, renderer, *args, **kwargs):
        query = self.DataSource.projectArray(self.axes)
        self.set_data(query.data)
        # look for repeating colormap setting
        # worry about colormaps when we think through how aesthetics 
        self.set_clim(query.data.min(), query.data.max()) # gets the colorbar Working
        self.set_extent(query.extent)
        
        # query for the right projecton
        super().draw(renderer, *args, **kwargs)
        
class ArrayLine(mcollections.LineCollection):
    def __init__(self, datasource, *args, **kwargs):
        super().__init__(None, *args, **kwargs)
        self.DataSource = datasource
        
    def draw(self, renderer, *args, **kwargs):
        query = self.DataSource.projectLine2D(self.axes)
        self.set_segments(query.data)
        super().draw(renderer, *args, **kwargs)
        
class ArrayBar(mcollections.PatchCollection):
    def 
    
class Array1Dhist:
    def __init(self):
        pass
