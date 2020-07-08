from types import SimpleNamespace
import numpy as np 

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
    
    # is bins aesthetic or computational
    def queryHist1D(self, ax, *args, flatten=True, bins='auto', **kwargs):
        if flatten == True:
            count, bins = np.histogram(self.data.ravel())
        else:
            raise NotImplementedError("Use self.queryXY")
        bp = Projection(bins, 1, bins.shape)
        cp = Projection(count, 1 , count.shape)
        return SimpleNamespace(bins=bp, count=cp)
        
