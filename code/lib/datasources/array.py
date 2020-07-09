from types import SimpleNamespace

import numpy as np 

from lib.datasources.core import  DataSource, Projection
        
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
        
