class MyHashMap:
    # use an array for O(1) time in all operations
    # space complexity depends on the number of keys stored
    def __init__(self):
        self.map = [-1] * 1000001
        

    def put(self, key: int, value: int) -> None:
        self.map[key] = value
        

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)