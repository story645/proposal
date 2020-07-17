from types import SimpleNamespace
import numpy as np 

import matplotlib.image as mimage
import matplotlib.collections as mcollections
import matplotlib.path as mpath
import matplotlib.markers as mmarkers
import matplotlib.transforms as mtransforms

# datasource maps D->Projection for artist (query)
# aesthetic maps P-> retinal variables (red, sqaure)
# artist maps retinal variables -> pixels (CW-complex)

# What artists end up:
#1. get plotting data (pull set of rows) - 
    # comes in as dict of bertin variables 
#2. dict of maps of floats to visual propeties
#    'size array' -> actual marker sizes
#    'data units' -> pixels
#3. push to vector model

def constraint_check(*args):
    pass
class Image(mimage.AxesImage):
    def __init__(self, ax, datasource, *args, **kwargs):
        """
        Parameters
        ----------
        ax: matplotlib.axes.Axes
            axes that data will be plotted on
        datasource: matplottoy.datasources.DataSource like
            data object containing data to be plotted
        **kwargs:
           kwargs passed through 
        """
        super().__init__(ax, *args, **kwargs)
        # self.constraints = constraint_check (self.DataSource.mappings, req, optional)
        # for attr in required_list:
        # assert(getattr(DataSource))
        
        #self.mappings = datasource.mappings()
        self.DataSource = datasource
        
    def draw(self, renderer):
        
        #projection = self.DataSource.query(ax, self.mappings)
    
        projection = self.DataSource.queryArray(self.axes)
        #update states we need to update
        self.set_data(projection.data.payload)
        # look for repeating colormap setting
        # worry about colormaps when we think through how aesthetics 
        self.set_clim(projection.data.payload.min(), 
                      projection.data.payload.max()) 
        # gets the colorbar working
        self.set_extent(projection.extent.payload)
        
        # query for the right projecton
        super().draw(renderer)


class Line(mcollections.LineCollection):
    def __init__(self, datasource, *args, **kwargs):
        """
        Parameters
        ----------
        datasource: matplottoy.datasources.DataSource like
            data object containing data to be plotted
        **kwargs:
            kwargs passed through 
        """
        super().__init__(None, *args, **kwargs)
        self.DataSource = datasource
        
    def draw(self, renderer, *args, **kwargs):
        projection = self.DataSource.queryXY(self.axes, xdim='unique')
        self.set_segments([np.vstack([x,y]).T 
                           for x,y in zip(projection.x.payload, 
                                          projection.y.payload)])
        super().draw(renderer, *args, **kwargs)

class Scatter(mcollections.Collection):
    def __init__(self, datasource, *args, **kwargs):
        """
        Parameters
        ----------
        datasource: matplottoy.datasources.DataSource like
            data object containing data to be plotted
        **kwargs:
        """
        super().__init__(*args, **kwargs)
        self.DataSource = datasource
    
    def draw(self, renderer, *args, **kwargs):
        projection = self.DataSource.queryXY(self.axes, xdim='unique')
        radius = kwargs.get('radius', .02)
        if radius is None:
            if projection.x.payload>1:
                radius*=10
        paths = []
        for (X, Y) in zip(projection.x.payload,projection.y.payload):
             paths.extend([mpath.Path.circle(center=(x,y), radius=radius)                           for (x,y) in zip(X,Y)])
        self._paths = paths
        self.set_edgecolors('k')
        super().draw(renderer, *args, **kwargs)

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
        super().__init__(*args, **kwargs)
        self.DataSource = datasource
        self.stacked = stacked
        
    def draw(self, renderer, *args, **kwargs):
        projection = self.DataSource.queryXY(self.axes, xdim='same')
        
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
