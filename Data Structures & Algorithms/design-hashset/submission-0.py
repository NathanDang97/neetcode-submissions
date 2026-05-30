class MyHashSet:
    # use an array for O(1) time in all operations
    # space complexity depends on the number of keys stored
    def __init__(self):
        self.hash_set = [False] * 1000001
        

    def add(self, key: int) -> None:
        self.hash_set[key] = True

    def remove(self, key: int) -> None:
        self.hash_set[key] = False

    def contains(self, key: int) -> bool:
        return self.hash_set[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)