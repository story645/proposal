from types import SimpleNamespace
import numpy as np

from array_datasource import DataSource, Projection


class DataSourceDataFrame(DataSource):
    def __init__(self, df, **kwargs):
        self.data = df
        self.dependent = kwargs.get('dependent', None)
        self.independent = kwargs.get('independent', None)
        
    @property
    def dependent(self):
        return self._dependent
    
    @dependent.setter
    def dependent(self, name):
        self._dependent = name

    @property
    def independent(self):
        return self._independent
    
    @independent.setter
    def independent(self, name):
        self._independent = name
        
    def queryXY(self, ax, *args, xdim=1):
        xp = Projection([self.data[self.dependent]], 1, len(self.data[self.dependent]))
        yp = Projection([self.data[self.independent]], 1, 
                       len(self.data[self.independent]))
        return SimpleNamespace(x=xp, y=yp)
 
    def queryHist1D(self, ax, *args, column = None, **kwargs):
        if column is None:
            count, bins = np.histogram(self.data.ravel())
        else:
            count, bins = np.histogram(self.data[column])
       
        bp = Projection(bins, len(bins), bins.shape)
        cp = Projection(count, len(count), count.shape)
        return SimpleNamespace(bins=bp, count=cp)