class SimplexPoint:
    # whole shape
    def __init__(self, coord):
        """one point in triangle or edge or whatever, class is whole simplex
        """
        coord = np.array(coord)
        # Needs to be postive and add to one
        assert (coord>=0).prod() > 0
        assert coord.sum() == 1
        self.coord = coord

class LocalFiberComponent: # F_i - type, spec, U\sigma
    def __init__(self, fiber_component=None):
        """
        fiber_componenet: value in F_i
        """
        self.fiber_component = fiber_component

class LocalFiberPoint: # F = F_0 X F
    def __init__(self, local_fiber_point=[LocalFiberComponent()]):
        """ return of \tau at one point in K - no base point yet
        is a point in F
        """
        self.local_fiber_point = local_fiber_point

class LocalSectionComponent: #\tau_i on an F_i (column wise indexing)
    """defining the bundle in terms of the datastructure that is holding it
    """
    def __init__(self, funct):
        self.funct = funct
    def __call__(self, base_point): 
        """
        k in K
        """
        return LocalFiberComponent(funct(base_point))

class LocalSection:# \tau on F at base_point
    def __init__(self, local_section_components=[lambda base_point: None]):
        """\tau = {\tau_o, \ldots ,\tau_n}
        """
        self.local_section_components = local_section_components

    def __call__(self,base_points):
        """ \tau 
            construct fiber based on data 
        """
        return [(base_point, 
                LocalFiberPoint([local_section_component(base_point)
                            for local_section_component in local_section_components]) 
                                for base_point in base_points]
