import functools

import numpy as np 
#taus

#TODO: write atleast_1d wrapper
class Identity:
    @staticmethod
    def convert(value):
        return value
    @staticmethod
    def validate(mtype):
        return mtype.mtype in ['nominal', 'ordinal', 'interval']
class Nominal:
    def __init__(self, mapping):
        self._mapping = mapping
        
    def convert(self, value):
        values = np.atleast_1d(np.array(value, dtype=object))
        return [self._mapping[v] for v in values]

    def validate(self, value):
        values = np.atleast_1d(np.array(value, dtype=object))
        return True