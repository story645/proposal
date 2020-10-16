c# constraints aren't checked, they're built into the assumptions
class DataSourceBase:
    def __init__(self, data, bertin_variables):
        pass
    def schema(self, ):
        # must be CONST over controllable 
        # contract between data source and artist
        # what bertin variables it can provide
        # shapes, topology, datatypes - .info()
        # https://www.modernescpp.com/index.php/c-core-guidelines-a-detour-to-contracts
        # for dataframe--
        # column names is bertin names - 
        # plus shape and dtypes and whatever
        # query returns subset of columns
    def mapping(self, ):
        pass
    def update(new_data):
        #check the schema 
        pass
    def query(self, bertin_variables):
        # stable 
        d[x]
        pass

class DataSourcePoint(DataSourceBase):
    pass

class DataSourceLine(DataSourceBase):
    # init enforces constraints for line plot
    def __init__(self, d, x, y, **optional):
        """ 
        d:
            data handle
        x: indexer/subset label
        y: indexer/subset label
        """
        # has to say x name is this 
        # has to say y name is this

    def query(self, bv):
        return {'x','y'}


class DataSourceArea(DataSourceBase):
    pass
 
