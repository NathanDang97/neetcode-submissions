class Solution:
    # one-pass solution, O(n) time, O(1) space
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum, curr_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum