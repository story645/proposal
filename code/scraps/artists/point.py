
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
        ## moved to a MarkerSize()
        if 's' in self.opt_encodings:
            radius = data_view.get('s')  
        else:
            radius = itertools.repeat(self._s)

        paths = []

        x = aes.x(data_view_get(''))
        y = aes.y(data.view_get(''))

        """
        #curry/partialized the mpath.Path.circle
        c = {}
        c['marker'] = mpath.Path.circle
        c['size'] = 5
        c['color'] = 'red'
        """
        for (x, y, r) in zip(data_view.get('x'), 
                             data_view.get('y'), 
                             radius):
            paths.append(c)

      
        self.__draw(renderer, *args, **kwargs)
    """
    def __draw(self):
            ## to __draw   
        for p in paths:
            func = p.pop('marker')
            p2.append(func(**p))
            paths.append(mpath.Path.circle(center=(x,y), radius=r))                         
        self._paths = aes.geo.get_paths('???')
        self.set_edgecolors('k')
        pass
    """