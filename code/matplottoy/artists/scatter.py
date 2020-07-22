import matplotlib.collections as mcollections

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