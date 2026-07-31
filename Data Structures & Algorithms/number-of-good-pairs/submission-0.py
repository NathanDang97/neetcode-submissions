from collections import defaultdict
class Solution:
    # frequency counter solution, O(n) time and space
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        num_pairs = 0
        for num in nums:
            # any new occurence of num can form a good pair with all previous occurences of num
            num_pairs += counter[num]
            counter[num] += 1
        return num_pairs