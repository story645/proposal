import numpy as np
def mnx(d):
    return np.min(d)-np.std(d) , np.max(d) + np.std(d)