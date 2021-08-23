from dataclasses import dataclass
from typing import Tuple, Optional, List

import numpy as np
import pandas as pd

# index is like the sheaf, stalk is either the fiber or the values? 
# check the applied category theory book 
# index is subset on K
# technically this can be wrapped even more
# 
# maybe make a Record type Record = {Fiber_Name: values} 
class DataFrameWrapper:
    def __init__(self, section: pd.DataFrame):
        self.global_section = section 

    def query(self, data_bounds:Optional[dict] = None, sampling_rate:int=None)->List[dict]:
        if data_bounds is not None:
        #  in theory this should be smarter to account for categorical...
            query_str = '&'.join(f'{k}>={vmin} & {k}<={vmax}' for (k, (vmin, vmax)) in data_bounds.items())
            local_section = self.global_section.query(query_str)
        else:
            local_section = self.global_section
        #theory would return list of local sections
        local_section = local_section.assign(default=np.nan)
        return [{Fi:local_section[Fi].values.squeeze() for Fi in local_section.columns}]