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

class Projection: 
    #this gets duck typed, push all logic into DataSourceArray
    def __init__(self, payload, nitems, shape):
        self.payload = payload
        self.nitems = nitems
        self.shape = shape
    
        
class DataSourceArray(DataSource):
    def __init__(self, arr):
        self.data = arr

    def queryArray(self, ax, *args):
        data = Projection(self.data, 1, self.data.shape)
        #.5 so 0,0 is at center of pixel
        extent = Projection([-.5, data.payload.shape[1]-.5, 
                             -.5, data.payload.shape[0]-.5],
                            1, (4))
        return SimpleNamespace(data=data, extent=extent)
    
    def queryXY(self, ax, *args, xdim=1):
        
        y, shape = zip(*[(yi, yi.shape) for yi in self.data.T])
        yp = Projection(y, len(y), shape) 
        
        # data source should provide the x 
        # data source knows the sampling rate
        if xdim == 1:
            x = [np.arange(len(self.data))]
        elif xdim =='y':
            x = [np.arange(len(yi)) for yi in y]
        else:
            raise ValueError("I need to know my dimensions")     
        xp = Projection(x, len(x), [xi.shape for xi in x])
        
        return SimpleNamespace(x=xp, y=yp)

class ArrayImage(mimage.AxesImage):
    def __init__(self, ax, datasource, *args, **kwargs):
        super().__init__(ax, *args, **kwargs)
        self.DataSource = datasource
        
    def draw(self, renderer, *args, **kwargs):
        projection = self.DataSource.queryArray(self.axes)
        self.set_data(projection.data.payload)
        # look for repeating colormap setting
        # worry about colormaps when we think through how aesthetics 
        self.set_clim(projection.data.payload.min(), 
                      projection.data.payload.max()) 
        # gets the colorbar Working
        self.set_extent(projection.extent.payload)
        
        # query for the right projecton
        super().draw(renderer, *args, **kwargs)
        
class ArrayLine(mcollections.LineCollection):
    def __init__(self, datasource, *args, **kwargs):
        super().__init__(None, *args, **kwargs)
        self.DataSource = datasource
        
    def draw(self, renderer, *args, **kwargs):
        projection = self.DataSource.queryXY(self.axes, xdim='y')
        self.set_segments([np.vstack([x,y]).T 
                           for x,y in zip(projection.x.payload, 
                                          projection.y.payload)])
        super().draw(renderer, *args, **kwargs)
                
class ArrayBar(mcollections.Collection):
    def __init__(self, datasource, stacked=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.DataSource = datasource
        self.stacked = stacked
        
    def draw(self, renderer, *args, **kwargs):
        projection = self.DataSource.queryXY(self.axes, xdim=1)
        
        xoffset = np.zeros(projection.y.nitems)
        width = 0.8
        #verts : n*2 array of xy pair of rectangle
        if not self.stacked:
            xoffset =  (np.arange(projection.y.nitems)/
                        projection.y.nitems)
            width = (width/projection.y.nitems)
        verts = []
        xshape, = projection.x.shape
        xpayload, = projection.x.payload
        bottoms = np.zeros(shape=xshape)
        for group, xoff in zip(projection.y.payload, xoffset):
            xleft = xpayload + xoff
            xright = xleft + width
            for xl, xr, bottom, height in zip(xleft, xright, bottoms, group):
                rectangle = [(xl, bottom), 
                             (xl, bottom+height), 
                             (xr, bottom+height), 
                             (xr, bottom), 
                             (xl, bottom)]
                verts.append(rectangle)
            if self.stacked:
                bottoms+=group
        #breakpoint()
        self._paths = [mpath.Path(xy, closed=True) for xy in verts]
        self.set_edgecolors('k')
        super().draw(renderer, *args, **kwargs)
        return
    
    
class Array1Dhist:
    def __init(self):
        pass
