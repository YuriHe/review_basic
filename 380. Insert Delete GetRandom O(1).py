import random

class RandomizedSet:
    """
    Question: OOP
    in order to execute by O(1) -> hashmap
    """
    def __init__(self):
        # create position map{num: index}
        self.pos = {}
        # create array store random num
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]
        # replace this val in values with last one, guarantee O(1)
        last = self.values[-1]
        self.values[idx]= last
        self.pos[last] = idx
        # after swap, remove val info
        del self.pos[val]
        # remove redundant last(since last already move to another place)
        self.values.pop()

        return True
    
    def getRandom(self) -> int:
        # either way is correct
        return random.choice(self.values)
        return self.values[randint(0, len(self.values)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()