from types import SimpleNamespace

import numpy as np

from matplottoy.datasources.core import  DataSource, Projection

from types import SimpleNamespace
from typing import Protocol

import numpy as np 
from matplottoy.datasources.core import  DataSource, Projection
"""
plot(x,y, ....transfroms)
sataSource
scatter(x,y,c, s...)
artist:
....s, markerstyle/edgestyle, ...
"""
class ArrayContainer:
    """does the unpacking
    {'x':0}...
    """
    DataSourcePoint(bundleofdata, [....])

{'x':dataframe[0], 'y'= array[2], 
'z': graph[j]}

C1, C2, C3 -> {(DataSource , Transfroms) -> Artist}
              {Line2D(**)}

class View:
    # rows are selected, data is all the same number of rows
    def __init__(self, data, m, encodings, ax=None):
        """contract w/ draw method, just the things the draw needs
        """
        self.ax = ax # everything has the same axes
        for key, col in encodings.items():
            setattr(self, key, data[col][m])

    def get(self, visual_var): # axis seperation of concern
        return getattr(self, visual_var)
        
def make_info(data, m, encodings):
    info = {'encodings': len(encodings)} 
    for key, col in encodings.items():
        var = data[col][m]
        info[key] = {'length': len(max),
                    'min': var.min(), 
                    'max': var.max(), 
                    'name': col}
    return info

{'x':0}, {('x', 'y'): LineEncoder}
{'x':(0, LineEncoder)}
{0:LineEncoder} <- signature checking
{'x':LineEcoder} <-Datasource
{'x': 0} <-DataContainer Level

# passing in a literal means using 
# default mpl transforms
# identity transform
# pass in two tuple w/ validate, transform

Artist: {'marker': markertransformer...}
{'markerfacecolor':colortransformer...}
{'markeredgecolor':colortransformer,
'color': 'orange', 'cmap': 'RdBu', 
'fec': TransformTuple(lambda *args, **kwargs: 'red', lambda *arg, **kwargs: pass)}

# encodings dict gets baked into data
# encodings_meta = {'x':{name:}}

class DataFramePoint:
    def __init__(self, data, m=None, encodings=None):
        """ 
        data: arraylike
            data that will be plotted, must have >= 2 columns
        m: indexer, default is all values
            list of rows to take
        encodings: dict, default None
            {retinal variable : data selecter}
            for full list of options, see:
            matplottoy.artist.point.Point.required
            matplottoy.artist.point.Point.optional
            x defaults to 0, y defaults to 1
        """
        # should axes go here - 
        # (since there's a top level controller anyway)
        # can only draw on the axes it's drawing on?
        self.data = data
        if m is None:
            m = self.data.index
        self.m = m
        self.encodings = encodings if encodings else {}
        if 'x' not in self.encodings:
            self.encodings['x'] = self.data.columns[0]
        if 'y' not in self.encodings:
            self.encodings['y'] = self.data.columns[1]

    @property
    def info(self):
        """Read only attribute providing information about the data 
        that can be used for labeling and axes formatting
        """
        if not hasattr(self, '_info'):  
            self._info['m'] = self.m
            self._update(make_info(self.data, self.m, self.encodings))
        return self._info

    def view(self, ax=None):
        return View(self.data, self.m, self.encodings, ax=ax)


class DataSourceDataFrame(DataSource):
    """"
    Provides a an interface to dataframes, assumes the sementics of 
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