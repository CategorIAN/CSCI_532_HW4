from functools import reduce
from MySet import MySet
import pandas as pd

class SetCollection:
    def __init__(self, collection, n = None):
        self.n = self.getn(collection) if n is None else n
        self.collection = collection
        self.totalContained = self.getSuperSetSize()

    def getSuperSetSize(self):
        superset = reduce(lambda s, k: s + self[k], self.collection.keys(), MySet(set()))
        return len(superset)

    def getn(self, collection):
        print("Getting n:")
        def getMax(m, k):
            s = collection[k]
            return m if len(s) == 0 else max(m, max(s))
        return reduce(getMax, collection.keys(), -1) + 1

    def __getitem__(self, key):
        return self.collection[key]

    def __repr__(self):
        return str(self.collection)

    def __str__(self):
        return str(self.collection)

    def __add__(self, mytuple):
        n = max(self.n, 0 if len(mytuple[1]) == 0 else max(mytuple[1]) + 1)
        return SetCollection(self.collection|dict([mytuple]), n)

    def covering(self):
        def go(size, covered, remaining, toRemove):
            #If the size of what is covered is the size of the total contained from the original collection, then stop.
            if size == self.totalContained:
                return covered
            else:
                def filterAndFind(reduced_max, k_s):
                    #We want to subtract the last set added to our covering from the remaining sets. This is our "filter".
                    mytuple = (k_s[0], k_s[1] - toRemove)
                    #We want to keep the largest set from our remaining sets after filtering. This is our "find".
                    mymax = mytuple if (reduced_max[1] is None or (mytuple[1] > reduced_max[1][1])) else reduced_max[1]
                    #We keep our remaining collection of sets filtered. We keep the max.
                    return (reduced_max[0] + mytuple, mymax)
                (reduced, toAdd) = reduce(filterAndFind, remaining.collection.items(), (SetCollection({}, 0), None))
                #We keep track how big our current covered set by adding the size of the added to the size.
                #We add the original set according to the max of the filtered by looking it up from the key of the max.
                #We keep keep looking through the remaining sets that are progressively filtered.
                #The set that was considered the max will be the next set to subtract from the remaining.
                return go(size + len(toAdd[1]), covered + (toAdd[0], self[toAdd[0]]), reduced, toAdd[1])
        return go(0, SetCollection({}, 0), SetCollection(self.collection, self.n), MySet(set()))

    def toCSV(self, file = "collection"):
        d = dict([(elem, [int(elem in self[k]) for k in self.collection.keys()]) for elem in range(self.n)])
        pd.DataFrame(d).to_csv("{}.csv".format(file))








