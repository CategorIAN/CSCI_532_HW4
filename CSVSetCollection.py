from SetCollection import SetCollection
from MySet import MySet
import pandas as pd
from functools import reduce

class CSVSetCollection (SetCollection):
    def __init__(self, file):
        df = pd.read_csv(file, index_col = 0)
        super().__init__(dict([(k, self.mySet(df, k)) for k in df.index]), len(df.columns))

    def mySet(self, df, key):
        addElem = lambda s, elem: s + MySet(key, {int(elem)}) if bool(df.at[key, elem]) else s
        return reduce(addElem, df.columns, MySet(key, set()))