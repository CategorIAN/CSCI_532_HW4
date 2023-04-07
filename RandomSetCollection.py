from SetCollection import SetCollection
from MySet import MySet
from functools import reduce
import random
from math import pow

class RandomSetCollection (SetCollection):
    def __init__(self, n):
        self.n = n
        m = random.randint(0, int(pow(2, n)))
        super().__init__(dict([(k, self.randomSet(k)) for k in range(m)]), n)

    def randomSet(self, key):
        addElem = lambda s, i: s + MySet(key, {i}) if random.choice([True, False]) else s
        return reduce(addElem, range(self.n), MySet(key, set()))




