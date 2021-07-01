Is `float` a unit?
- matplotlibs units are maybe nu convertors based on type inference
- are units part of the type definition, specifying constraints on types, or something different?
- are floats and units the same type of thing? (H says yes, T says no)
- enums - class StopLight: Red->Yellow->Green->Red is the type definition, equivariant nu would have to be map between StopLight and some class with similar structure class X: x1->x2->x3->x4
- for units, equivariance constraints include requirements that conversion maps from->to same type of physical unit, for example 
    - inches->centimeter: works
    - inches->watts: breaks equivariance
- where does Spivak fit in?
    - H: `float` != `inch` != `meter`, - these are all unique types, but the actions on inch are the same as the actions on meter, which are not the same as the ones on float
        - float actions: permutation, ordering, translation, scaling
        - meter/inch actions: float actions + actions specific to length (like physical objct)
    - spivaks copies allow for reuse of base type (is C1, C2 map to the same DT)
        - meter to inch conversion can be f from C -> C' :
            C->f->C'
       sigma \  / sigma '
              DT
