from functools import partial
from types import SimpleNamespace

import numpy as np 

import matplotlib.collections as mcollections

from matplottoy.artists.core import check_constraints
class Line(mcollections.LineCollection):
    required = {'y'}
    optional = {'x'}

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

        assert (self.keys.encodings==self.transforms.keys())

        for key in encodings:
            assert self.transforms[key].validate(data.info[key])

        # check transforms via signature matching
        # check transforms via validation

    def draw(self, renderer, *args, **kwargs):
        data_view = self.data.view(self.axes) 
        #curried out
        if 'x' in self.opt_encodings:
            x = partial(data_view.get, 'x')   
        else:
            x = partial(np.arange, self.data.view.m['observations'])

        'xy' =  np.vstack([x(), data_view.get('y')]).T

        for key in opt_encodings:
            c[key] = append(self.transfroms.key.transform(...))
    
        # maps from idealised to insanity
        # down the line don't want the 
        # __draw(**c) 
        
    def __draw(components):
        # make_composites(c) <- 
        """collect all the like parameters
        markerstyle, markerface, etc
        """"
        self.set_segments(components('xy'))
                           
        super().draw(renderer, *args, **kwargs)
