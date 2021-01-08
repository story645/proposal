import functools

import numpy as np 
#taus

#TODO: write atleast_1d wrapper
class Identity:
    @staticmethod
    def convert(value):
        return np.array(value)
    @staticmethod
    def validate(mtype):
        return mtype in ['nominal', 'ordinal', 'interval', 'ratio']

class Log:
    def __init__(self, base=10):
        self.base = base

    def convert(self, value):
        return np.log(value)/np.log(self.base)

    def validate(self, mtype):
        return True
class Nominal:
    def __init__(self, mapping):
        self._mapping = mapping
        
    def convert(self, value):
        values = np.atleast_1d(np.array(value, dtype=object))
        return np.array([self._mapping[v] for v in values])

    def validate(self, mtype):
        return True