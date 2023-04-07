
class MySet:
    def __init__(self, key, set):
        self.key = key
        self.set = set

    def __repr__(self):
        return str(self.set)

    def __len__(self):
        return len(self.set)

    def __iter__(self):
        for each in self.set:
            yield each

    def __lt__(self, other):
        return len(self.set) < len(other.set)

    def __add__(self, other):
        return MySet(self.key, self.set.union(other.set))

    def __sub__(self, other):
        return MySet(self.key, self.set.difference(other.set))

