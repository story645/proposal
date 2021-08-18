from dataclasses import dataclass

import numpy as np
import pandas as pd



# index is like the sheaf, stalk is either the fiber or the values? 
# check the applied category theory book 
# index is subset on K
# technically this can be wrapped even more 

@dataclass
class FruitSection:
    K = 'integer'
    F = {'fruit': np.dtype('O'), 
               'calories': np.dtype('int64'), 
               'juice': np.dtype('bool')}
    section: pd.DataFrame

    def __post_init__(self):
        #check the fiber is a subset
        if not (self.section.dtypes.to_dict().items() <= self.F.items()):
            raise TypeError(f"{self.section.dtypes.to_dict()} not in fiber {self.F}")
        # checking on type since section doesn't have to be global
        if self.section.index.inferred_type != 'integer':
            raise TypeError(f"{self.section.index.inferred_type} is not type {self.K}")

    def local_section(self, data_bounds=None): #query
        """
        # this is BAD!
        data_bounds: {'fiber_key', (data_min, data_max)}
        """
        data_bounds = {} if data_bounds is None else data_bounds
        mask = '&'.join(f'{k}>={vmin} & {k}<={vmax}' for (k, (vmin, vmax)) in data_bounds.items())
        return FruitSection(self.section.query(mask))
    
    def projection(self, fiber_name=None):
        return FruitSection(self.section.get(fiber_name).to_frame())

    def values(self): #view
        """a compute method or something could be stashed here
        is the resolution stage
        """
        return self.section.values




def fiberbundle(section): #dataframe is section, type annotations
    """K and F can be defined here, 
    0or as part of a type defintion for section,  
    if want to check that section is part of the fiber bundle"""

    #split c in half to keep to preserve data/visual split, 
    # this is b/c we don't have direct S->K
    # matplotlib doesn't want to know everyone's indexing method  

    def view(subsets): # inverse nu should happen to the artist - just bounding boxes {fiber, subset in data coordinates}
        """axes is a restriction on the index, maybe it's xi
        might be xi, might be the index/axes subsetting
        index comes from the section/is part of the FB definition 
        """
        #define it as filtering is optional
        index = section.section.index# in theory can subselect here on info from the axes
        def projection(column_name):
            def values(): #
                if column_name is None:
                    return pd.Series(index=index, dtype=float)
                return section.section[column_name][index]
            return values 
        return projection
    return view
