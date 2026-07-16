import random
from collections import defaultdict

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.pos = defaultdict(set)

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        existed = len(self.pos[val]) > 0
        self.arr.append(val)
        self.pos[val].add(len(self.arr) - 1)
        return not existed

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not self.pos[val]:
            return False

        idx = self.pos[val].pop()
        last = self.arr[-1]

        if idx != len(self.arr) - 1:
            self.arr[idx] = last
            self.pos[last].remove(len(self.arr) - 1)
            self.pos[last].add(idx)

        self.arr.pop()

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()