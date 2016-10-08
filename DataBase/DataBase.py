""" The file that create the DataBase and launch the query

...
"""

import inspect, os
file_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) #
import pandas as pa


class DataBase:
    def __init__(self):
        # The __init__ create the load the DataBase using Panda
        self.data = pa.read_csv(file_path + '/data/LPI_pops_restricted_20160421.csv')

        print(self.data.head(n=1))



    def query(self,keyword):
        self.data =