import numpy as np 

import matplotlib.colors as mcolors
class Position:
    @staticmethod
    def convert(value):
        return value
    @staticmethod
    def validate(mtype):
        return mtype.mtype in ['nominal', 'ordinal', 'interval']
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
