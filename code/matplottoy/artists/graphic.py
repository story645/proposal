from dataclasses import dataclass, field
from typing import List, Any

import matplotlib.path as mpath
import matplotlib.transforms as mtransforms

from matplottoy.encoders import mtypes

@dataclass 
class Graphic:
    path: mpath.Path
    transform: mtransforms.Transform
    offset: Any=None
    offsetTrans: mtransforms.Transform=None
    facecolor: mtypes.RGBA
    edgecolor: mtypes.RGBA
    linewidth: mtypes.LineWidth
    linestyle: mtypes.LineStyle
    antialiased: bool=True
    url: str=None
    offset_position: str='screen'

@dataclass
class GraphicCollection:
    paths: List[mpath.Path]
    transforms: List[mtransforms.Transform]
    offsets: List[Any]
    offsetTrans: List[mtransforms.Transform]
    facecolors: List[mtypes.RGBA]
    edgecolors: List[mtypes.RGBA] 
    linewidths: List[mtypes.LineWidth]
    linestyles: List[mtypes.LineStyle] 
    antialiaseds: [bool]l,.
    urls: List[str]
    offset_position: str='screen'
