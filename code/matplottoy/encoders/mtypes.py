"""Specifying the objects passed into the renderer
"""

from dataclasses import dataclass
@dataclass
class RGBA:
    r: float
    g: float
    b: float
    a: float = 1.0
    def __post_init__(self):
        assert all((0 <= x <= 1.0) for x in [self.r, self.g, self.b, self.a])

@dataclass
class LineStyle: #replace w/ Bruno's version
    style: str = 'solid'
    
@dataclass
class LineWidth:
    width: float = 1.0
    def __post_init__(self):
        assert self.width>0

