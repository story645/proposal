from collections import defaultdict

import numpy as np

import mtypes
 
class FiberBundle:
    """Sets up the definition of the fiber bundle
    """
    #k values are constant for a fixed fiber bundle
    rng = np.random.default_rng(12345)
    def __init__(self):
        self.K = {'ndims': 0, 
                  'keys': self.rng.choice(10**5, size=1000, replace=False)}
        self.F = {'v1': mtypes.Ordinal(range(1,6)), 
                  'v2': mtypes.Interval([0,10]),
                  'v3': mtypes.Nominal(['true', 'false'])}
        

class Section(FiberBundle):
    """Inherits the schema and topology from F because it by definition 
       doesn't have a different one if it's a fiber on F
    """
    def __init__(self):
        super().__init__()

    def sigma(self, k):
        """Returns the piece of the section at k"""
        # set of functions for choosing values from F at a given k
        # is usually the data structure
        rng = np.random.default_rng(k*1000)
        return (k, (rng.choice(self.F['v1'].categories), 
                    rng.uniform(self.F['v2'].min, self.F['v2'].max),
                    rng.choice(self.F['v3'].categories)))
    def table(self):
        """helper method to create a Table b/c a 
        datastructure object is what the artist should work on
        """
        data = {}
        for k in self.K['keys']:
            data[k] = dict(zip(self.F.keys(), self.sigma(k)[-1])) 
        return Table(self.K, self.F, data)
class Table:
    def __init__(self, topology, schema, data):
        """
        data is passed in as a nested dict {k: {column name:value}}
        what gets passed into the artist is a data container object
        """
        super().__init__()
        for (index, row) in data.items():
            assert index in topology['keys']
            for (col, val) in row.items():
                assert schema[col].validate(val)
        self.K = topology
        self.F = schema
        self.data = data

    def view(self):
        """"converts data into atomic column order 
        for get method"""
        table = defaultdict(list)
        for (index, row) in self.data.items():
            table['index'].append(index)
            for (col, val) in row.items():
                table[col].append(val)
        return table
