from types import SimpleNamespace
import numpy as np 

import matplotlib.collections as mcollections

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