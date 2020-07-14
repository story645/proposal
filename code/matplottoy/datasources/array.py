from types import SimpleNamespace

import numpy as np 

from lib.datasources.core import  DataSource, Projection
        
class DataSourceArray(DataSource):
    def __init__(self, arr):
        """
        Parameters
        ----------
        arr : ArrayLike, size=(M,N)
        """
        self.data = arr

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
        extent = Projection([-.5, data.payload.shape[1]-.5, 
                             -.5, data.payload.shape[0]-.5],
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
        if xdim == 'x':
            x = [np.arange(len(self.data))]
        elif xdim =='y':
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