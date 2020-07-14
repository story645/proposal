from types import SimpleNamespace

import numpy as np

from lib.datasources.core import  DataSource, Projection

class DataSourceDataFrame(DataSource):
    """"
    Provides a an interface to dataframes, assumes the semenatics of 
    dependent and independent variables
    """
    def __init__(self, df, **kwargs):
        """
        Parameters:
        df : DataFrameLike, size=(observations, columns)
        **kwargs
            dependent: str
                name of column containing dependent variable
            independent: str
                name of column containing independent variable
        """
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


        
    def queryXY(self, ax=None, *args):
        """
        Parameters
        ----------
        ax: matplotlib.axes.Axes
            axes that the data will be plotted on
        
        Returns
        -------
        SimpleNamespace:
            attributes: Projection objects
                xp: dependent column values
                yp: independent column values
        """
        xp = Projection([self.data[self.dependent]], 1, len(self.data[self.dependent]))
        yp = Projection([self.data[self.independent]], 1, 
                       len(self.data[self.independent]))
        return SimpleNamespace(x=xp, y=yp)
 
    def queryHist1D(self, ax=None, *args, **kwargs):
        """
        Parameters
        ----------
        ax: matplotlib.axes.Axes
            axes that data will be plotted on
        **kwargs:
            'variable' str
                name of column for which histogram is being computed

        """
        variable = kwargs.pop('variable', None)
        if variable == 'dependent':
            count, bins = self.data[self.dependent].hist()
        elif variable == 'independent':
            count, bins = self.data[self.independent].hist()
        else:
             count, bins = np.histogram(self.data.data.ravel())
                
    
        bp = Projection(bins, len(bins), bins.shape)
        cp = Projection(count, len(count), count.shape)
        return SimpleNamespace(bins=bp, count=cp)