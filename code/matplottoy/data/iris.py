import pandas as pd

from matplottoy.data.simplex import FiberBundle
from matplottoy.encoders import mtypes

class Projection: #sheaf? stalk? presheaf? 
    def __init__(self, index, handle, fiber): # should be subset K + tau
        self.index =  index
        self.handle = handle
        self.fiber = fiber

    def __call__(self):
        if self.fiber is None:
            return pd.Series(index=self.index, dtype=float)
        return self.handle[self.fiber]


# index is like the sheaf, stalk is either the fiber or the values? 
# check the applied category theory book 
# index is subset on K
def fiberbundle(section): #dataframe is section
    def subset_k(axes): 
        """axes is a restriction on the index, maybe it's xi
        might be xi, might be the index/axes subsetting
        index comes from the section/is part of the FB definition 
        """
        index = section.index# in theory can subselect here on info from the axes
        def projection(column_name):
            def values(): #
                if column_name is None:
                    return pd.Series(index=index, dtype=float)
                return section[column_name][index]
            return values 
        return projection
    return subset_k #set k.. in K that tau is applied to 

class DataFrame:
    def __init__(self, dataframe):
        self.FB = FiberBundle(K = {'tables':['vertex']},
                              F = dict(dataframe.dtypes))
        self._tau = dataframe.iloc
        self._view = dataframe #use this for column wise indexing

    def view(self, fibers, axes=None):
        # axes modifies the sheaf rules (index)
        return [Projection(self._view.index, self._view, fiber) for fiber in fibers]
class Iris:
    FB = FiberBundle({'tables': ['vertex']},
                     {'species': str,
                      'sepal_length':  float,
                      'sepal_width': float,
                      'petal_length': float,
                      'petal_width': float,
                      'sepal_length_color': mtypes.RGBA,
                      'sepal_width_color': mtypes.RGBA,
                      'petal_length_color': mtypes.RGBA,
                      'petal_width_color': mtypes.RGBA
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


