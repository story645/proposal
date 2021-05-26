from matplottoy.data.simplex import FiberBundle
from matplottoy.encoders import mtypes

class DataFrame:
    def __init__(self, dataframe):
        self.FB = FiberBundle(K = {'tables':['vertex']},
                              F = dict(dataframe.dtypes))
        self._tau = dataframe.iloc
        self._view = dataframe

    def view(self, axes=None):
        return self._view
    
    
class Iris:
    FB = FiberBundle({'tables': ['vertex']},
                     {'species': mtypes.Nominal({'setosa', 'versicolor', 'virginica'}),
                      'sepal_length':  mtypes.IntervalRatio(),
                      'sepal_width': mtypes.IntervalRatio(),
                      'petal_length': mtypes.IntervalRatio(),
                      'petal_width': mtypes.IntervalRatio(),
                      'sepal_length_color': mtypes.Color(),
                      'sepal_width_color': mtypes.Color(),
                      'petal_length_color': mtypes.Color(),
                      'petal_width_color': mtypes.Color()
                      })
    def __init__(self, dataframe):
        for column in dataframe:
            if not all(self.FB.F[column].validate(v) for v in dataframe[column]):
                raise ValueError(f'{column} has values that are invalid {self.FB.F[column]}')
        
        self.sigma = dataframe.iloc
        self._view = dataframe

    def view(self, simplex="vertex"):
        return self._view




class FrequencyBar:
    """Wraps precomputed data
    """                 
    K = {'tables': ['vertex']}

    def __init__(self, categories, counts):
        assert len(categories) == len(counts)
        F = {'category': mtypes.Nominal(set(categories)), 
             'count': mtypes.PositiveInteger()}
        
        self.FB = FiberBundle(self.K, F)

        self.categories = categories
        self.counts = counts        

    def view(self, simplex="vertex"):
        return  {'category': self.categories, 'count': self.counts}     


