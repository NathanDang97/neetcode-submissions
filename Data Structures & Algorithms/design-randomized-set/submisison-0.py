import random
class RandomizedSet:
    # O(n) space
    # O(1) time for getRandom(), O(n) time for insert() and remove() but O(1) in average
    def __init__(self):
        self.idx_dict = defaultdict(int)
        self.lst = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.idx_dict:
            return False
        self.lst.append(val)
        self.idx_dict[val] = len(self.lst) - 1 # 0-indexed
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.idx_dict:
            # swap the last element to the index/position of the element to delete
            last, idx = self.lst[-1], self.idx_dict[val]
            self.lst[idx], self.idx_dict[last] = last, idx

            # delete the last element
            self.lst.pop()
            del self.idx_dict[val]
            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.lst)