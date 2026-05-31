class Solution:
    # sliding window solution, O(n) time, O(1) space
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        l, r = 0, 0
        curr_sum = 0
        while r < len(nums):
            curr_sum += nums[r]
            while curr_sum >= target:
                min_length = min(min_length, r - l + 1)
                curr_sum -= nums[l]
                l += 1
            r += 1

        return min_length if min_length != float('inf') else 0