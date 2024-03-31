class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        try:
            # key already exists in the map, update it
            index =  self.keys.index(key)
            self.values[index] = value
        except:
            # key is not in the map. 
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        try:
            # key exists in the map, return its value
            index =  self.keys.index(key)
            return self.values[index]
        except:
            # key is not in the map
            return -1

    def remove(self, key: int) -> None:
        try:
            # key exists in the map, remove it and its value
            index = self.keys.index(key)
            self.keys.pop(index)
            self.values.pop(index)
        except:
            # key is not in the map
            return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)