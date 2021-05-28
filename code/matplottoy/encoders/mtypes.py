"""Formally defining measurement types (from Stevens)
to check against visual channels
"""
# if validate overwrites is instance, then we can 
# use float/int/etc...
from dataclasses import dataclass, field
from typing import List, Tuple, Iterable

import matplotlib.colors as mcolors

@dataclass
class RGBA:
    r: float
    g: float
    b: float
    a: float=1
    
    def __post__init__(self):
        assert all(0 <= x <= 1 for x in [self.r, self.g, self.b, self.a])

@dataclass
class LineWidth:
    linewidth:float=1
    
    def __post__init__(self):
        assert(self.linewidth>0)
        
@dataclass
class LineStyle: #
    offset: float=0
    offsetseq: Tuple[float, ...]=field(default_factory=lambda:())
    
    def __post__init__(self):
        assert (self.offset>=0)
        assert(all(x>=0 for x in self.offsetseq))
        assert(len(self.offsetseq)% 2==0)