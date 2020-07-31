from types import SimpleNamespace
from typing import Protocol

import numpy as np 
from matplottoy.datasources.core import  DataSource, Projection


# set of visual variables that each geometry 
# supports
# versus set of each visual literals each bertin 

class View:
    # rows are selected, data is all the same number of rows
    def __init__(self, data, m, encodings, ax=None):
        self.ax = ax # everything has the same axes
        for key, col in encodings.items():
            var = data[m, col]
            setattr(self, key, var)

    def get(self, visual_var): # axis seperation of concern
        return getattr(self, visual_var)

class ArrayLine:
    def __init__(self, data, m=Ellipsis, encodings=None):
        """ 
        data: arraylike
            data that will be plotted, must have >= 2 columns
        m: indexer, default is all values
            list of rows to take
        encodings: dict, default None
            {retinal variable : data selecter}
            for full list of options, see:
            matplottoy.artist.line.Line.required
            matplottoy.artist.line.Line.optional
            y defaults to 0
        """
        # encodings = {'x':0, 'y':1, 'color': 'color'}
        # should axes go here - 
        # (since there's a top level controller anyway)
        # can only draw on the axes it's drawing on?
        self.data = data
        self.m = m
        self.encodings = encodings if encodings else {}
        self.encodings['y'] = self.encodings.get('y', 0)

    @property
    def info(self):
        """Read only attribute providing information about the data 
        that can be used for labeling and axes formatting
        """
        if (not hasattr(self, '_info') or 
            (self.m != self._info['observation_indexer'])):  
            self._info = {'encodings': len(self.encodings), 
                          'observation_indexer': self.m} 
            for key, col in self.encodings.items():
                var = self.data[self.m, col]
                self._info[key] = {'type': var.dtype, 
                                  'shape': var.shape,
                                    'min': var.min(), 
                                    'max': var.max(), 
                                   'name': col}
        return self._info
        
    def view(self, ax=None):
        return View(self.data, self.m, self.encodings, ax=ax)
class ArrayPoint:
    def __init__(self, data, m=Ellipsis, encodings=None):
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
        self.m = m
        self.encodings = encodings if encodings else {}
        if 'x' not in self.encodings:
            self.encodings['x'] = 0
        if 'y' not in self.encodings:
            self.encodings['y'] = 1

    @property
    def info(self):
        """Read only attribute providing information about the data 
        that can be used for labeling and axes formatting
        """
        if not hasattr(self, '_info'):  
            self._info = {'encodings': len(self.encodings)} 
            for key, col in self.encodings.items():
                var = self.data[self.m, col]
                self._info[key] = {'type': var.dtype, 
                                  'shape': var.shape,
                                    'min': var.min(), 
                                    'max': var.max(), 
                                   'name': col}
        return self._info

    def view(self, ax=None):
        return View(self.data, self.m, self.encodings, ax=ax)

class DataSourceArray(DataSource):
    def __init__(self, arr, transpose = False):
        """
        DataSource array makes the assumption that data is
        oriented (N,M) where N is number of observations and 
        M is the number of measurement types 
        
        Parameters
        ----------
        arr : ArrayLike, size=(M,N)
        transpose: False, optional
            True: transpose the input data
        """
        if transpose:
            self.data = arr.T
        else:
            self.data = arr
        self.mappings = {}

    def query(self, ax=None, mappings=None):
        for mas in mappings:
            pass

    def queryArray(self, ax=None, *args):
        """
        Parameters
        ----------
        ax: matplotlib.axes.Axes
            axes that data will be plotted on
        
        Returns
        -------
        SimpleNamespace
            attributes: Projection objects
                data - data to be plotted
                extent - view limits of the data:
                     (in axes? coordinates)
        """
        data = Projection(self.data, 1, self.data.shape)
        #.5 so 0,0 is at center of pixel
        extent = Projection((-.5, data.payload.shape[1]-.5, 
                             -.5, data.payload.shape[0]-.5),
                            1, (4))
        return SimpleNamespace(data=data, extent=extent)
    
    def queryXY(self, ax=None, *args, xdim = 'same'):
        """
        Parameters
        ----------
        ax: matplotlib.axes.Axes
            axes that data will be plotted on
        xdim: str
            'same': use the same list of x values 
                    for every column of y values in the
                     input array
            'unique': use a unique list of x values 
                    for each column of y values in the 
                    input array
        Returns
        -------
        SimpleNamespace
            attributes: Projection Objects
                xp: list of x values for plot
                    xdim: 'same' (1 list of size M)
                    xdim: 'unique' (N lists of size M)
                yp: list of y values for plot (N lists of size M)
        """
        y, shape = zip(*[(yi, yi.shape) for yi in self.data.T])
        yp = Projection(y, len(y), shape) 
        
        # data source should provide the x 
        # data source knows the sampling rate
        if xdim == 'same':
            x = [np.arange(len(self.data))]
        elif xdim =='unique':
            x = [np.arange(len(yi)) for yi in y]
        else:
            raise ValueError("I need to know my dimensions")     
        xp = Projection(x, len(x), [xi.shape for xi in x])
        
        return SimpleNamespace(x=xp, y=yp)
    
    # is bins aesthetic or computational
    def queryHist1D(self, ax, *args, flatten=True, bins='auto', **kwargs):
        """
        Parameters
        ----------
        ax: matplotlib.axes.Axes
            axes that data will be plotted on
        flatten: Bool, True or False
            True: flatten the array before computing the histogram
            False: compute a histogram for each column in the array
        bins: str (how do we handle these vis/artist properties)
            bin argument passed through to `numpy.histogram`
        **kwargs
        Returns
        -------
        SimpleNamespace
            attributes: Projection Objects
                bins: histogram bins  
                counts: counts of binned data
        """
        if flatten == True:
            counts, bins = np.histogram(self.data.ravel(), bins=bins)
        else:
            raise NotImplementedError("Use self.queryXY")
        bp = Projection(bins, 1, bins.shape)
        cp = Projection(counts, 1 , count.shape)
        return SimpleNamespace(bins=bp, counts=cp)