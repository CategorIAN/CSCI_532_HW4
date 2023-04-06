from SetCollection import SetCollection
from MySet import MySet
from functools import reduce
import random

class RandomSetCollection (SetCollection):
    def __init__(self, n):
        pass

    def createMySet(self, key, bools):
        addElem = lambda s, i: s + MySet(key, {i}) if bools[i] else s
        return reduce(addElem, range(len(bools)), MySet(key, set()))


