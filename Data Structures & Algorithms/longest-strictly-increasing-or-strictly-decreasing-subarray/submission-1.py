class Solution:
    # one-pass solution, O(n) time, O(1) space
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase, decrease = 1, 1
        longest = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                increase = decrease = 1
            elif nums[i] > nums[i - 1]:
                increase += 1
                decrease = 1
            else:
                increase = 1
                decrease += 1
            longest = max(longest, increase, decrease)

        return longest