import functools

import numpy as np 

import matplotlib.colors as mcolors
#taus

#TODO: write atleast_1d wrapper
class Position:
    @staticmethod
    def convert(value):
        return value
    @staticmethod
    def validate(mtype):
        return mtype.mtype in ['nominal', 'ordinal', 'interval']

class NominalPosition:

    def __init__(self, mapping):
        self._mapping = mapping
        
    def convert(self, value):
        values = np.atleast_1d(np.array(value, dtype=object))
        return [self._mapping[v] for v in values]

    def validate(self, value):
        values = np.atleast_1d(np.array(value, dtype=object))
        return True

###write at least1d wrapper
class IdentityColor:
    @staticmethod
    def convert(value):
        values = np.atleast_1d(np.array(value, dtype=object))
        return [mcolors.to_rgba(v) for v in values]

    @staticmethod
    def validate(mtype):
        return all(mcolors.is_color_like(v) for v in mtype.categories)

class NominalColor:
    def __init__(self, mapping):
        """goal of init is to store parameters that would otherwise be
        curried higher level function"""
        self._mapping = mapping

    def convert(self, value):
        values = np.atleast_1d(np.array(value, dtype=object))
        return [mcolors.to_rgba(self._mapping[v]) for v in values]

    def validate(self, mtype):
        return (set(mtype.categories) == self._mapping.keys() and
        all(mcolors.is_color_like(color) for color in self._mapping.values()))

