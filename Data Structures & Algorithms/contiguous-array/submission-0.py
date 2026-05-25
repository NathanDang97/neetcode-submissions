from collections import defaultdict
class Solution:
    # hash map solution, time and space O(n)
    def findMaxLength(self, nums: List[int]) -> int:
        # maps prefix sum to the *earliest* index it was seen
        prefix_sum_map = defaultdict(int)
        prefix_sum_map[0] = -1 # sum of 0 exists before we begin
        max_length, prefix_sum = 0, 0

        for i, num in enumerate(nums):
            # treat 0 as -1 so that a sum of 0 means same number of 0s and 1s
            prefix_sum += 1 if num == 1 else -1
            if prefix_sum in prefix_sum_map:
                # if the sum was seen before, the subarray in between the current 
                # index i and the stored index in the map is balance
                max_length = max(max_length, i - prefix_sum_map[prefix_sum])
            else:
                # only store the earliest occurence to maximize the length
                prefix_sum_map[prefix_sum] = i

        return max_length