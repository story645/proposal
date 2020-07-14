from types import SimpleNamespace

def user_plotting_method(data):
    # user a .describe instead of is instance...
    if not isinstance(data, DataSource):
        datasource= DataSource(data) # goes through registry

class Projection: 
    #this gets duck typed, push all logic into DataSourceArray
    def __init__(self, payload, nitems, shape):
        """
        Parameters
        ----------
        payload: 
            data to be plotted
        nitems: 
            number of unique variables/attributes to be plotted
            eg. line plot of an array where every column is a line
        shape:
            total shape of the data
        """
        self.payload = payload
        self.nitems = nitems
        self.shape = shape

class DataSource: #set of classes replaces _preprocess_data
    # documents interface 
    pass 

class DataSourceDict(DataSource):
    pass # assume this is like a dataframe, labels = columns
class DataSourceDictView(DataSource):
    pass
class Enums(DataSource):
    # name, value pair where value can contain multiples
    pass