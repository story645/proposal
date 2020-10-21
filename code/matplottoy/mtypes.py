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
        self.categories = categories
        self.min = min(categories)
        self.max = max(categories)

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