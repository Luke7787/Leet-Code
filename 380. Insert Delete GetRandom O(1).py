import random

class RandomizedSet(object):

    def __init__(self):
        self.data = []
        self.index = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.data:
            return False
        self.data.append(val)
        self.index[val] = len(self.data)-1
        return True
        
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.data:
            return False
        last_data = self.data[-1]
        index = self.index[val]
        self.data[index] = last_data
        self.index[last_data] = index
        self.data.pop()
        del self.index[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.data)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()