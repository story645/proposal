
import itertools

from matplotlib import rcParams
import matplotlib.collections as mcollections
import matplotlib.path as mpath

from matplottoy.artists.core import check_constraints
class Point(mcollections.Collection):
    required = {'x', 'y'}
    optional = {'s'} 
    
    def __init__(self, datasource, *args, **kwargs):
        """
        Parameters
        ----------
        datasource: matplottoy.datasources.DataSource like
            data object containing data to be plotted
        **kwargs:
        """
        # do we set defaults at this level?
        # else is rcparams markersize 
        self._s = kwargs.pop('s') if 's' in kwargs else rcParams['lines.markersize']/10
        super().__init__(*args, **kwargs)
        
        check_constraints(self.required, self.optional, 
                         datasource.encodings.keys())
        self.opt_encodings = (datasource.encodings.keys() - 
                                Point.required)
        self.data = datasource

        
    def draw(self, renderer, *args, **kwargs):
        # loop to do aesthetic encoding stuff w/ pitching
        data_view = self.data.view(self.axes)
        #grab i
        if 's' in self.opt_encodings:
            radius = data_view.get('s')  
        else:
            radius = itertools.repeat(self._s)
        paths = []
        for (x, y, r) in zip(data_view.get('x'), 
                             data_view.get('y'), 
                             radius):
            paths.append(mpath.Path.circle(center=(x,y), radius=r))                         
        self._paths = paths
        self.set_edgecolors('k')
        super().draw(renderer, *args, **kwargs)