class MyHashMap(object):

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key, value):
        if key in self.keys:
            index = self.keys.index(key)
            self.values[index] = value
        else:
            self.keys.append(key)
            self.values.append(value)


    def get(self, key):
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        else:
            return -1

    def remove(self, key):
        if key in self.keys:
            index = self.keys.index(key)
            self.keys.pop(index)
            self.values.pop(index)
        else:
            return -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)