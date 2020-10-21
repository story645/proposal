"""Formally defining measurement types (from Stevens)
to check against visual channels
"""
class Nominal: 
    mtype = 'nominal'
    def __init__(self, categories):
        self.categories = categories
    def validate(self, value):
        return value in self.categories

class Ordinal:
    mtype = 'ordinal'
    def __init__(self, categories):
        self.categories = self._has_ordering(categories)
    
    def _has_ordering(self, categories):
        # should really be explicit if it has ordering
        return categories

    def validate(self, value):
        return value in self.categories

class Interval:
    mtype = 'interval'
    def __init__(self, interval):
        assert len(interval)==2
        self.min = min(interval)
        self.max = max(interval)
    
    def validate(self, value):
        return (self.min<=value) & (value<=self.max)