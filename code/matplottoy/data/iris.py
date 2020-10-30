import data
import mtypes

class Iris:
    FB = data.FiberBundle({'tables': ['vertex']},
                     {'species': mtypes.Nominal({'setosa', 'versicolor', 'virginica'}),
                      'sepal_length':  mtypes.IntervalRatio(),
                      'sepal_width': mtypes.IntervalRatio(),
                      'petal_length': mtypes.IntervalRatio(),
                      'petal_width': mtypes.IntervalRatio(),
                      })
    def __init__(self, dataframe):
        for column in dataframe:
            assert all(self.FB.F[column].validate(v) for v in dataframe[column])
        
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
        
        self.FB = data.FiberBundle(self.K, F)

        self.categories = categories
        self.counts = counts        

    def view(self, simplex="vertex"):
        return  {'category': self.categories, 'count': self.counts}     


