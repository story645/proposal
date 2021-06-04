from dataclasses import dataclass, field
from typing import List, Any

import matplotlib.path as mpath
import matplotlib.transforms as mtransforms

from matplottoy.encoders import mtypes

@dataclass 
class Graphic:
    path: mpath.Path
    transform: mtransforms.Transform
    facecolor: mtypes.RGBA
    edgecolor: mtypes.RGBA
    linewidth: mtypes.LineWidth
    linestyle: mtypes.LineStyle
    antialiased: bool=True
    url: str=None
    offset_position: str='screen'
    offset: Any=None
    offsetTrans: mtransforms.Transform=None


@dataclass # this is kinda mu
class PatchConfig: #kind of base it on existing mpl mark parameters
    position: [float] #feeds label
    length: Iterable[float] 
    floor: Iterable[float] = field(default_factory = lambda: [0]) 
    width: Iterable[float] = field(default_factory = lambda: [.8])
    offset: Iterable[float] = field(default_factory = lambda: [0])
    facecolors: Iterable[mtypes.RGBA] = field(default_factory = 
                                        lambda: [mtypes.RGBA( .12, .46, .71, 1)])
    edgecolors: Iterable[mtypes.RGBA] = field(default_factory = 
                                        lambda: [mtypes.RGBA(0, 0, 0, 1)])
    linewidths: Iterable[mtypes.LineWidth] = field(default_factory = 
                                        lambda: [mtypes.LineWidth()])
    linestyles: Iterable[mtypes.LineStyle] = field(default_factory = 
                                        lambda: [mtypes.LineStyle()])
    def __post__init__(self):
        assert len(position) == len(floor)
@dataclass # this is kinda rho
class GraphicCollection: #push the draw specific stuff up to v
    paths: List[mpath.Path]
    transforms: List[mtransforms.Transform]
    offsets: List[Any]
    offsetTrans: List[mtransforms.Transform]
    facecolors: List[mtypes.RGBA]
    edgecolors: List[mtypes.RGBA] 
    linewidths: List[mtypes.LineWidth]
    linestyles: List[mtypes.LineStyle] 
    antialiaseds: [bool]
    urls: List[str]
    offset_position: str='screen'
