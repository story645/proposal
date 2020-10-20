import random
import numpy as np


class DiscreteToyTable:
    rng = np.random.default_rng()
    def __init__(self, N=1000, max_key=10**5):
        assert max_key>N
        self.K = self.rng.choice(max_key, size=N, replace=False)
        # F is the space of all possible values
        # the schema defines F
        self.F = ({'type':'discrete-ordinal', 'values':range(1,6)}, 
                  {'type':'continuous', 'interval':[0,10]}, 
                  {'type':'discrete', 'values':['true', 'false']})    

    def sigma(self, k):
        """Returns the section at K"""
        # set of functions for choosing values from F at a given k
        # is usually the data structure
        return (k, (random.sample(self.F[0]['values'], k=1)[0],
                    self.rng.uniform(self.F[1]['interval'][0], 
                                     self.F[1]['interval'][1]), 
                    random.sample(self.F[2]['values'], k=1)[0]))

class Transform:
    @staticmethod
    def x(value):
        return value
    @staticmethod
    def y(value):
        return value
    @staticmethod
    def color(value):
        return "red"