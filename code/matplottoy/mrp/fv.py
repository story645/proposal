import numpy as np

class DiscreteToyTable:
    def __init__(self, N=1000, max_key=10**15):
        self.K = np.random.randint(0, max_key, num_keys)
        self.schema = {'x': {'type':'continuous', 'interval':[0, 100]} 
                       'y': {'type':'continuous', 'interval':[200, 300]}
                       'color': {'type':'discrete', 'values':['happy','sad']}}
        self.data = 
