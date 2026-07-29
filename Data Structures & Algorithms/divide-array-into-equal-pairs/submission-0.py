from collections import defaultdict
class Solution:
    # frequency counting solution, O(n) time and space
    def divideArray(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        for num, count in counter.items():
            if count % 2 != 0:
                return False

        return True