class View: # want an atomic snapshot
# get returns part of coherant dataset
# rows are selected, data is all the same number of rows
    def __init__(self, data, m, ax=None):
        """contract w/ draw method, just the things the draw needs
        """
        self.ax = ax # everything has the same axes
        
        for key, data in encodings.items():
            setattr(self, key, data)
    # get can't happen w/o view
    def get(self, visual_var): # axis seperation of concern
        return getattr(self, visual_var)


df = pd.DataFrame(np.cumsum(
                  np.tile([1., 2., .03, 5.], reps=100).reshape(100,4), axis=0), 
                  columns = ['odds', 'evens','threes', 'fives'])

encodings_meta({'x': {'min', 'max', 'shape'} )
Data({'x': df['odds']}, self.m, encodings_meta=None)

M = {'edges': tuple pairs,
    'verts' : N or list((vertices),
    'k':,}

F = ['heterogenous', 'homogenous', 'univariate']
# N + edges = 0 has to be discrete
# N + edges 1 has to be continuous 1D

class Data:
    def __init__(self, encodings, encodings_meta = None):
        """ 
        """
        # should axes go here - 
        # (since there's a top level controller anyway)
        # can only draw on the axes it's drawing on?
        self.data = data
        self.encodings = encodings if encodings else {}

        if encodings_meta.keys()>= encodings.keys():
            raise Warning(f"Meta provided for unencoded keys 
                            {encodings_meta.keys() - encoded.keys()}")
        self._info = {'encodings':encodings.keys()}

        if 'm' in encodings_meta:
            raise ValueError("Invalid Key: m")
        self._info[m] = self.m

    @property
    def info(self):
        """Read only attribute providing information about the data 
        that can be used for labeling and axes formatting
        """
        if self._info['m'] != self.m:
            # somehow data should provide a way to update into
            raise Warning("key no longer valid") 
        return self._info

    def view(self, ax=None):
        return View(self.data, self.m, ax=ax)
    
