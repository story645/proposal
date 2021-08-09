from dataclasses import dataclass

import numpy as np
import pandas as pd



# index is like the sheaf, stalk is either the fiber or the values? 
# check the applied category theory book 
# index is subset on K
# technically this can be wrapped even more 

@dataclass
class Section:
    F =  {'fruit': np.dtype('O'), 
               'calories': np.dtype('int64'), 
               'juice': np.dtype('bool')}
    K =  pd.core.indexes.range.RangeIndex

    section: pd.DataFrame

    def __post_init__(self):
        #check the fiber matches
        assert self.section.dtypes.to_dict() == self.F
        # checking on type since section doesn't have to be global
        assert isinstance(self.section.index, self.K)


def fiberbundle(section): #dataframe is section, type annotations
    """K and F can be defined here, 
    0or as part of a type defintion for section,  
    if want to check that section is part of the fiber bundle"""

    #split c in half to keep to preserve data/visual split, 
    # this is b/c we don't have direct S->K
    # matplotlib doesn't want to know everyone's indexing method  
    def projection(column_name):
        def subset_k(subsets): # inverse nu should happen to the artist - just bounding boxes {fiber, subset in data coordinates}
            """axes is a restriction on the index, maybe it's xi
            might be xi, might be the index/axes subsetting
            index comes from the section/is part of the FB definition 
            """
            #define it as filtering is optional
            index = section.section.index# in theory can subselect here on info from the axes
            def values(): #
                if column_name is None:
                    return pd.Series(index=index, dtype=float)
                return section.section[column_name][index]
            return values 
        return subset_k
    return projection
