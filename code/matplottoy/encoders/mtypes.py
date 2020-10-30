"""Formally defining measurement types (from Stevens)
to check against visual channels
"""
# if validate overwrites is instance, then we can 
# use float/int/etc...

class Nominal: 
    mtype = 'nominal'
    shape = 'scaler'
    def __init__(self, categories):
        self.categories = categories
    def validate(self, value):
        return value in self.categories

class Ordinal:
    mtype = 'ordinal'
    def __init__(self, categories):
        self.categories = categories
        self.min = min(categories)
        self.max = max(categories)

    def validate(self, value):
        return value in self.categories
class PositiveInteger:
    mtype = 'ordinal'
    def validate(self, value):
        return value>=0
class IntervalRatio:
    mtype = 'interval'
    def __init__(self, floor=0):
        self.floor = floor
    def validate(self, value):
        return value>=self.floor

class IntervalClosed:
    mtype = 'interval'
    def __init__(self, interval):
        assert len(interval)==2
        self.min = min(interval)
        self.max = max(interval)
    
    def validate(self, value):
        return (self.min<=value) & (value<=self.max)
