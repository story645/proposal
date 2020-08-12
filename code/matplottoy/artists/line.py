from functools import partial
from types import SimpleNamespace

import numpy as np 

import matplotlib.collections as mcollections

from matplottoy.artists.core import check_constraints
class Line(mcollections.LineCollection):
    required = {'y'}
    optional = {'x', 'edges'}

    def __init__(self, datasource, transfrom_functions=None, *args, **kwargs):
        """
        Parameters
        ----------
        datasource: matplottoy.datasources.DataSource like
            data object containing data to be plotted
        **kwargs:
            kwargs passed through 
        """
        super().__init__(None, *args, **kwargs)
        
        check_constraints(self.required, self.optional, 
                          datasource.encodings.keys())
             
        #how to refactor this into all the thing
        self.opt_encodings = (datasource.encodings.keys() - 
                                Line.required)
        self.data = datasource


    def draw(self, renderer, *args, **kwargs):
        data_view = self.data.view(self.axes) 
        #curried out
        if 'x' in self.opt_encodings:
            x = partial(data_view.get, 'x')   
        else:
            x = partial(np.arange, self.data.info['y']['length'])
            
        self.set_segments([np.vstack([x(), data_view.get('y')]).T])
                           
        super().draw(renderer, *args, **kwargs)
