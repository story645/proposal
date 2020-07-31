from types import SimpleNamespace
import numpy as np 

import matplotlib.collections as mcollections

class Line(mcollections.LineCollection):
    required = {'y'}
    optional = {'x'}

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
        
        check_constraints(self.required, self.optional, 
                          datasource.encodings.keys())
        
        self.opt_encodings = (datasource.encodings.keys() - 
                                Line.required)
        self.data = datasource


    def draw(self, renderer, *args, **kwargs):
        data_view = self.data.view(self.axes) 

        y = data_view.get('y')
        
        if 'x' in self.opt_encodings:
            x = data_view.get('x')   
        else:
            x = np.arange(len(y))

        self.set_segments([np.vstack([x,y]).T 
                           for x,y in zip(projection.x.payload, 
                                          projection.y.payload)])
        super().draw(renderer, *args, **kwargs)