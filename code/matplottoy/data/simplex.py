from collections import defaultdict
from dataclasses import dataclass
import itertools
import numpy as np
from matplottoy.encoders import mtypes
 
@dataclass
class FiberBundle:
    """
    Attributes
    ----------
    K: dict
        attributes of the base space of the fiber bundle, 
        describes domain of base space + the type of simplexs
        on the base space
        {'tables': []}

    F: dict
        the fiber, which is the space of all possible observations 
        type is used here to describe the space 
        {variable name: type}

    # rework as ('field name': (type, monoid action))
    """
    K:dict 
    F:dict
        # should maybe be folded into K
        # add check for consistency

    def is_section(self, section):
        """checks if a section is from a given fiber bundle:
        are values in F, are keys in K"""
        raise NotImplementedError()

class VertexSimplex: #maybe change name to something else
    """Fiberbundle is consistent across all sections
    Section = set of points in the base space restricted to  
    some k's in K
    """
    FB = FiberBundle({'tables': ['vertex']},  
                     {'v1': {'type': int, 'monoid': 'ordinal', 
                             'range': [1,2,3,4,5]},
                      'v2': {'type': float,'monoid':'interval',
                             'range': [0,1]},
                      'v3': {'type': str, 'monoid':'nominal', 
                             'range':['true', 'false']},
                      'v4': {'type': float, 'monoid':'interval', 
                             'range':[2,3]}       
                        })

    def __init__(self, sid = 45, size=1000, max_key=10**10):
        self.section_id = sid
        # keys should be in the domain of keys defined on K
        # in this case that's integers, also keys are fixed on 
        # a section
        rng = np.random.default_rng(sid)
        self.keys = rng.integers(0,max_key, size)

    def tau(self, k):
        """Returns the (k, obs) at k"""
        # set of functions for choosing values from F at a given k
        # is usually the data structure
        rng = np.random.default_rng(k*self.section_id)
        e1 = rng.choice(self.FB.F['v1']['range'])
        e2 = rng.uniform(*self.FB.F['v2']['range'])
        e3 = rng.choice(self.FB.F['v3']['range'])
        e4 = rng.uniform(*self.FB.F['v4']['range'])
        return (k, (e1, e2, e3, e4))

    def view(self, axes=None):
        """"converts data into atomic column order for get method
        # maybe also pass in the columns?
        """
        table = defaultdict(list)
        for k in self.keys:
            table['index'] = k
            for (name, value) in zip(self.FB.F.keys(), self.tau(k)[1]):
                table[name].append(value)
        return table



class EdgeSimplex: # ToDo: generalize to take list of functions as input
    """ Functions are part of the definition of the data, 
    Schema describes the types of the output value (basically 
    a continousish vertex table)

    line is telling me how I'm connected

    the static methods are sigmas on the section, 
    not dependent on the exact instance of the section
    """

    FB = FiberBundle({'tables': ['vertex','edge']},
                     {'x' : {'type:':float, 'monoid':'interval', 'range':[-1,1]},
                      'y':  {'type:':float, 'monoid':'interval', 'range':[-1,1]},
                      'color': {'type':mtypes.RGBA, 'monoid':'nominal', 
                                'range': ['red', 'green', 'orange', 'blue']}
                    })

    def __init__(self, num_edges=4, num_samples=1000):
        """which simplex am I on and distance""" 
        # define the k and distance 
        self.keys = range(num_edges)
        self.num_samples = num_samples
        self.distances = np.linspace(0,1, num_samples)
        # concession to this is a half generlized representation of 
        # arcs on a circle
        self.angle_samples = np.linspace(0, 2*np.pi, len(self.keys)+1)
    

    @staticmethod
    def _color(edge):
        colors = ['red','orange', 'green','blue']
        return colors[edge%len(colors)]

    @staticmethod
    def _xy(edge, distances, start=0, end=2*np.pi):
        """function that generates arc on x
        passes in edge (first part of k tuple)
        """
        # start and end are parameterizations b/c really there is 
        # one _xy function  per edge 

        angles = (distances *(end-start)) + start
        return np.cos(angles), np.sin(angles)

        
    def tau(self, k):
        """arbitrary k, even between vertices, will give back
        an observation, so all functions must target back to vertice 
        table
        Parameters:
        k: vertex or edge id
        technically simplex should be embedded in the k
        """
        #distances along edge are stored as self.distances
        #self.angle_samples
        x, y = self._xy(k, self.distances, self.angle_samples[k], self.angle_samples[k+1]) 
        return (k, (x, y, self._color(k)))

    def view(self, axes=None):
        table = defaultdict(list)
        for k in self.keys:
            table['index'].append(k)
            for (name, value) in zip(self.FB.F.keys(), self.tau(k)[-1]):
                table[name].append(value)
        return table

def is_continuous(vertices):
    """The adjacency matric for continous line is diagonal"""
    N = len(vertices)
    adj_mat = np.zeros((N,N))
    for (start, end) in vertices:
        # start col is 0-3, end col is 1-4
        adj_mat[start, end-1]+=1
    # making an assumption here that vertices define 
    # intervals along the 1D number line
    return (adj_mat == np.diag(np.diagonal(adj_mat))).all()

class GraphLine:
    def __init__(self, FB, edge_table, vertex_table, num_samples=1000, connect=False):
        self.FB = FB
        self.num_samples = num_samples
        self.distances = np.linspace(0,1, num_samples)
        if connect:
            assert edge_table.keys() == self.FB.F.keys()
            assert is_continuous(vertex_table)
        for  (column, functions) in edge_table.items():
            fiber_set = self.FB.F[column]['range']
            for f in functions:
                #check using random point along [0,1]
                assert all([min(fiber_set)<=v<=max(fiber_set) 
                            for v in np.atleast_1d(f(np.random.random()))])

        self.ids = range(len(vertex_table))
        self.vertices = vertex_table        
        self.edges = edge_table
        self.connect = connect

    def tau(self, k):
        """this function knows that there are functions on the fibers defined in F"""
        return(k, (self.edges[c][k](self.distances) for c in self.FB.F.keys()))

    def view(self, axes=None):
        """walk the edge_vertex table to return the edge value
        """
        # continuity test asserted one source, one sink 
        # sort here on sources (can also sort on sink)
        table = defaultdict(list)
        #since intervals lie along number line and are ordered pair neighbors
        #sort on start or end should yield ordering
        for (i, (start, end)) in sorted(zip(self.ids, self.vertices), key=lambda v:v[1][0]):
            table['index'].append(i)
            for (name, value) in zip(self.FB.F.keys(), self.tau(i)[1]):
                table[name].append(value)

        return table