from types import SimpleNamespace
import numpy as np 

import matplotlib.collections as mcollections
import matplotlib.path as mpath

class Bar(mcollections.Collection):
    def __init__(self, datasource, stacked=False, *args, **kwargs):
        """
        Parameters
        ----------
        datasource: matplottoy.datasources.DataSource like
            data object containing data to be plotted
        stacked: bool, optional
            True: bar chart is stacked (groups are added)
            False: bar chart is unstacked (groups are interspersed)
        orientation: str, optional
            vertical: bars aligned along x axis, heights on y
            horizontal: bars aligned along y axis, heights on x
        **kwargs:
            kwargs passed through 
        """
        self.stacked = stacked
        self.width = kwargs.pop('width', .8)
        super().__init__(*args, **kwargs)
        self.DataSource = datasource
  
        
    def draw(self, renderer, *args, **kwargs):
        projection = self.DataSource.queryXY(self.axes, xdim='same')
        
        xoffset = np.zeros(projection.y.nitems)
        #verts : n*2 array of xy pair of rectangle
        if not self.stacked:
            xoffset =  (np.arange(projection.y.nitems)/
                        projection.y.nitems)
            width = (self.width/projection.y.nitems)
        else:
            width = self.width
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
    
class Hist1D(mcollections.Collection):
    def __init__(self, datasource, *args, **kwargs):
        """
        Parameters
        ----------
        datasource: matplottoy.datasources.DataSource like
            data object containing data to be plotted
        **kwargs:
            kwargs passed through to Bar
        """
        self.DataSource = datasource
        self._orientation = kwargs.pop('orientation', 'vertical')
        # must sort through better keyword passing
        self._variable = kwargs.pop('variable', None)
        super().__init__(*args, **kwargs)
        
    def draw(self, renderer, *args, **kwargs):
        projection = self.DataSource.queryHist1D(self.axes, flatten=True, variable=self._variable, **kwargs)
        if projection.bins.shape[0] != (projection.counts.shape[0]+1):
            raise ValueError("should have 1 more bin than count")
        verts = []
        if self._orientation == 'vertical':
            xshape, = projection.bins.shape
            xpayload = projection.bins.payload
            bottom = 0
            for i, height in enumerate(projection.counts.payload):
                xl, xr = xpayload[i], xpayload[i+1]
                rectangle = [(xl, bottom), 
                             (xl, bottom+height), 
                             (xr, bottom+height), 
                             (xr, bottom), 
                             (xl, bottom)]
                verts.append(rectangle)
        else:
            yshape, = projection.bins.shape
            ypayload = projection.bins.payload
            bottom = 0
            for i, height in enumerate(projection.counts.payload):
                ybot, ytop = ypayload[i], ypayload[i+1]
                rectangle = [(bottom, ybot), 
                             (bottom, ytop), 
                             (height, ytop),
                             (height, ybot), 
                             (bottom, ybot)]
                verts.append(rectangle)
        self._paths = [mpath.Path(xy, closed=True) for xy in verts]            
        self.set_edgecolors('k')
        super().draw(renderer, *args, **kwargs)
        return
