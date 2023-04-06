

class SetCollection:
    def __init__(self, collection):
        if self.valid(collection):
            self.collection = sorted(collection, reverse=True)
            self.dictionary = dict([(s.key, s) for s in collection])
        else:
            raise Exception("Not Unique Keys")

    def valid(self, collection):
        def go(keys, collecting):
            if len(collecting) == 0:
                return True
            else:
                mySet = collecting[0]
                return mySet.key not in keys and go(keys|mySet.key, collecting[1:])
        return go(set(), collection)

    def __add__(self, myset):
        return SetCollection(self.collection + [myset])

    def remove(self, myset):
        return SetCollection([s - myset for s in self.collection])

    def restore(self, reduced_collection):
        return SetCollection([self.dictionary[k] for k in reduced_collection.dictionary.keys()])





