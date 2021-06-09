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


@dataclass # this is kinda mu?
class RectangleCollection: #kind of base it on existing mpl mark parameters
    x0: [float] #these are not general
    x1: Iterable[float] 
    y0: Iterable[float] 
    y1: Iterable[float] 
    facecolors: Iterable[mtypes.RGBA]
    edgecolors: Iterable[mtypes.RGBA] 
    linewidths: Iterable[mtypes.LineWidth] 
    linestyles: Iterable[mtypes.LineStyle] 

@dataclass # this is kinda rho?
class DrawPathCollection: #this is what gets passed off to the renderer Draw
    paths: List[mpath.Path] # is the path or the position the V? since the path is the glyph?
    transforms: List[mtransforms.Transform]
    offsets: List[Any]
    offsetTrans: List[mtransforms.Transform]
    facecolors: List[mtypes.RGBA]
    edgecolors: List[mtypes.RGBA] 
    linewidths: List[mtypes.LineWidth]
    linestyles: List[mtypes.LineStyle] 
    antialiaseds: [bool]
    urls: List[str]
    offset_position: str='screen' #data kwarg is deperecated
