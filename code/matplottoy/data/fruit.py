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
        # in this specific case, is easier to check that they're the same type
        assert isinstance(self.section.index, self.K)



def fiberbundle(section): #dataframe is section
    """K and F can be defined here, 
    0or as part of a type defintion for section,  
    if want to check that section is part of the fiber bundle"""

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
    return subset_k #s