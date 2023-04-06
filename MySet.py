
class MySet:
    def __init__(self, key, set):
        self.key = key
        self.set = set

    def __lt__(self, other):
        return len(self.set) < len(other.set)

    def __add__(self, other):
        return MySet(self.key, self.set.union(other.set))

    def __sub__(self, other):
        return MySet(self.key, self.set.difference(other.set))

