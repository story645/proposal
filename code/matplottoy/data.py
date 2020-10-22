from collections import defaultdict

import numpy as np

import mtypes
 
class FiberBundle:
    def __init__(self, K, F, K_in_F):
        """
        Parameters
        ----------
        K: dict
            attributes of the base space of the fiber bundle, 
            describes domain of base space + the type of simplexs
            on the base space
            {'simplexes':{}, domain: type }
        F: dict
            the fiber, which is the space of all possible observations 
            type is used here to describe the space 
            {variable name: type}
        K_in_F: dict
            mapping of which variables lie on which type of simplex:
            {simplex: [variable names]}
        """
        self.K = K 
        self.F = F
        self.K_in_F = K_in_F
        ###check if is consistent

    def is_section(section):
        """checks if a section is from a given fiber bundle:
        are values in F, are keys in K"""
        raise NotImplementedError()

class Section:
    """Inherits the schema and topology from F because it by definition 
       doesn't have a different one if it's a fiber on F
    """
    FB = FiberBundle({'simplexes':{'vertices'},  'domain': int},  
                     {'v1': mtypes.Ordinal(range(1,6)), 
                      'v2': mtypes.IntervalClosed([0,10]),
                      'v3': mtypes.Nominal(['true', 'false'])},
                     {'vertices': {'v1', 'v2', 'v3'}})

    def __init__(self, sid = 45, size=1000, max_key=10**10):
        self.section_id = sid
        # keys should be in the domain of keys defined on K
        # in this case that's integers, also keys are fixed on 
        # a section
        rng = np.random.default_rng(sid)
        self.keys = rng.integers(0,max_key, size)

    def sigma(self, k):
        """Returns the piece of the se, section at k"""
        # set of functions for choosing values from F at a given k
        # is usually the data structure
        rng = np.random.default_rng(k*self.section_id)
        return (k, (rng.choice(self.FB.F['v1'].categories), 
                    rng.uniform(self.FB.F['v2'].min, 
                                self.FB.F['v2'].max),
                    rng.choice(self.FB.F['v3'].categories)))

    def view(self):
        """"converts data into atomic column order for get method
        """
        table = defaultdict(list)
        for k in self.keys:
            table['index'] = k
            for (name, value) in zip(self.FB.F.keys(), self.sigma(k)[1]):
                table[name].append(value)
        return table


            