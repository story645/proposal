from types import SimpleNamespace
import numpy as np 

import matplotlib.image as mimage

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