from types import SimpleNamespace
import numpy as np 

import matplotlib.image as mimage
import matplotlib.collections as mcollections
import matplotlib.path as mpath

# datasource maps D->Projection for artist (query)
# aesthetic maps P-> retinal variables (red, sqaure)
# artist maps retinal variables -> pixels (CW-complex)

# axis, axes, legend...

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
    
    #variable x
    def projectnXnY(self, ax, *args):
        # data source should provide the x since data source knows the sampling rate
        y = [y for y in self.data.T]  
        x = [np.arange(len(yi)) for yi in y]
        return SimpleNamespace(x=x, y=y)
    #fixed X
    def project1XnY(self, ax, *args):
        x = np.arange(len(self.data))
        y = [y for y in self.data.T] # rows are group 
        return SimpleNamespace(x = x, y = self.data)

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
        query = self.DataSource.projectnXnY(self.axes)
        self.set_segments([np.vstack([x,y]).T 
                           for x,y in zip(query.x, query.y)])
        super().draw(renderer, *args, **kwargs)
        
class ArrayBar(mcollections.Collection):
    def __init__(self, datasource, stacked=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.DataSource = datasource
        self.stacked = stacked
        
    def draw(self, renderer, *args, **kwargs):
        query = self.DataSource.project1XnY(self.axes)
        #query.data needs to return - group , height, xpos
       
        xoffset = np.zeros(len(query.y))
        width = 0.8
        #verts : n*2 array of xy pair of rectangle
        if not self.stacked:
            xoffset =  np.arange(len(query.y))/len(query.y) 
            width = (width/len(query.y))
        verts = []
        bottoms = np.zeros(len(query.x))
        for group, xoff in zip(query.y, xoffset):
            xleft = query.x + xoff
            xright = xleft + width
            for x, height in zip(query.x, group):
                rectangle = [(xleft, 0), (xleft, height), 
                             (xright + height), (xright, 0)]
                verts.append(rectangle)
    
        self._path = [mpath.Path(xy, closed=True) for xy in verts]
        pass
    
    
    
    
class Array1Dhist:
    def __init(self):
        pass
