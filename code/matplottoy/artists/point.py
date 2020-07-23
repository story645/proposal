
import matplotlib.collections as mcollections
import matplotlib.path as mpath

class Point(mcollections.Collection):
    required = {'x', 'y'}
    optional = {'s'} 
    
    def __init__(self, input, *args, **kwargs):
        """
        Parameters
        ----------
        datasource: matplottoy.datasources.DataSource like
            data object containing data to be plotted
        **kwargs:
        """
        # do we set defaults at this level?
        # else is rcparams markersize 
        self._s = kwargs.pop('s') if 's' in kwargs else 10
        super().__init__(*args, **kwargs)
        
        self.check_constraints(datasource)
        self.opt_encodings = (datasource.encodings.keys() - 
                                Point.required)
        self.datasource = datasource
   
    #goes in matplotlib cbook
    def check_constraints(self, datasource):
        # check required encodings are there
       assert Point.required <= datasource.view.encodings.keys()
       # check optional encodings 
       assert ((datasource.view.encodings.keys() - Point.required) 
                <= Point.optional)
        
    def draw(self, renderer, *args, **kwargs):
        #.view will use m for automaticity
        data = self.datasource.view(self.axes)

        # loop to do aesthetic encoding stuff w/ pitching
        radius = data.get('s') if 's' in self.opt_encodings else self._s

        paths = []
        for (x, y, r) in zip(data.get('x'), data.get('y'), radius):
            paths.append(mpath.Path.circle(center=(x,y), radius=r))                         
        self._paths = paths
        self.set_edgecolors('k')
        super().draw(renderer, *args, **kwargs)