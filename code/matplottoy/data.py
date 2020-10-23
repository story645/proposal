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
            k is a tuple (which simplex)
                         (which simplex, which line)
                         (which simplex, face x, face y)
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
        # should maybe be folded into K
        # add check for consistency

    def is_section(self, section):
        """checks if a section is from a given fiber bundle:
        are values in F, are keys in K"""
        raise NotImplementedError()

class VertexSimplex: #maybe change name to something else
    """Fiberbundle is consistent across all sections
    Section = set of points in the base space restricted to  
    some k's in K
    """
    FB = FiberBundle({'domain': int},  
                     {'v1': mtypes.Ordinal(range(1,6)), 
                      'v2': mtypes.IntervalClosed([0,10]),
                      'v3': mtypes.Nominal(['true', 'false'])})

    def __init__(self, sid = 45, size=1000, max_key=10**10):
        self.section_id = sid
        # keys should be in the domain of keys defined on K
        # in this case that's integers, also keys are fixed on 
        # a section
        rng = np.random.default_rng(sid)
        self.keys = rng.integers(0,max_key, size)

    def sigma(self, k):
        """Returns the (k, obs) at k"""
        # set of functions for choosing values from F at a given k
        # is usually the data structure
        rng = np.random.default_rng(k*self.section_id)
        return (k, (rng.choice(self.FB.F['v1'].categories), 
                    rng.uniform(self.FB.F['v2'].min, 
                                self.FB.F['v2'].max),
                    rng.choice(self.FB.F['v3'].categories)))

    def view(self, simplex):
        """"converts data into atomic column order for get method
        """
        if simplex not in self.FB.K_in_F:
            return {}
        table = defaultdict(list)
        for k in self.keys:
            table['index'] = k
            for (name, value) in zip(self.FB.F.keys(), self.sigma(k)[1]):
                if name in self.FB.K_in_F[simplex]:
                    table[name].append(value)
        return table


class Simplex:
    """ Functions are part of the definition of the data, 
    Schema describes the types of the output value (basically 
    a continousish vertex table)

    line is telling me how I'm connected
    """

    FB = FiberBundle({'domain': int}, 
                     {'x' : mtypes.IntervalClosed([-np.inf, np.inf]),
                      'y':  mtypes.IntervalClosed([-np.inf, np.inf]),
                      'color': mtypes.Nominal(['red', 'green', 'orange', 'blue'])})

    def __init__(self, num_verts=4):
        """which simplex am I on and distance""" 
        # define the k and distance 
        self.keys = range(num_verts)

    def _color(edge):
        return  ['red', 'green', 'orange', 'blue'][edge]
    
    def _xy(edge):
        """function that generates arc on x"""
        #modify this so that the function 
        return np.sin_k, np.cos_k
        
    def sigma(self, k):
        """arbitrary k, even between vertices, will give back
        an observation, so all functions must target back to vertice 
        table
        Parameters:
        k: (edge, distance)
        k, distance
        """
        # split out sigma_vertex, sigma_edge
        # each edge needs to know which vertex it's between
        # sigma functions by definition evaluated on 0-1
        
        sinx, cosy = _xy(edge)
        sinx(distance)
        cosx(distance)
        return (x, y , _color(k))

    def view(self, simplex):
        if simplex not in self.FB.K_in_F:
            return {}
        table = defaultdict(list)
        for k in self.keys:
            table['index'] = k
            for (name, value) in zip(self.FB.F.keys(), self.sigma(k)[1]):
                if name in self.FB.K_in_F[simplex]:
                    table[name].append(value)
        return table
