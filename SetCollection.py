from functools import reduce
from MySet import MySet
import pandas as pd

class SetCollection:
    def __init__(self, collection, n = None):
        self.n = self.getn(collection) if n is None else n
        self.collection = collection
        self.totalContained = self.getSuperSetSize()

    def getSuperSetSize(self):
        superset = reduce(lambda s, k: s + self.__getitem__(k), self.collection.keys(), MySet(0, set()))
        return len(superset)

    def getn(self, collection):
        print("Getting n:")
        def getMax(m, k):
            s = collection[k]
            if len(s) == 0:
                return m
            else:
                return max(m, max(s))
        return reduce(getMax, collection.keys(), -1) + 1

    def __getitem__(self, key):
        return self.collection[key]

    def __repr__(self):
        return str(self.collection)

    def __str__(self):
        return str(self.collection)

    def __add__(self, myset):
        n = max(self.n, 0 if len(myset) == 0 else max(myset) + 1)
        return SetCollection(self.collection|{myset.key: myset}, n)

    def covering(self):
        def go(size, covered, remaining, toRemove):
            if size == self.totalContained:
                return covered
            else:
                def filterAndFind(reduced_max, k):
                    myset = remaining[k] - toRemove
                    mymax = myset if reduced_max[1] is None else max(reduced_max[1], myset)
                    return (reduced_max[0] + myset, mymax)
                (reduced, toAdd) = reduce(filterAndFind, remaining.collection.keys(), (SetCollection({}, 0), None))
                return go(size + len(toAdd), covered + self.__getitem__(toAdd.key), reduced, toAdd)
        return go(0, SetCollection({}, 0), SetCollection(self.collection, self.n), MySet(-1, set()))

    def toCSV(self, file = "collection"):
        d = dict([(elem, [int(elem in self.__getitem__(k)) for k in self.collection.keys()]) for elem in range(self.n)])
        pd.DataFrame(d).to_csv("{}.csv".format(file))








