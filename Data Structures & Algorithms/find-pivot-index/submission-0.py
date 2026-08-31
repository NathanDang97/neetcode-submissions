class Solution:
    # prefix sum solution, O(n) time, O(1) space
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        prefix_sum = 0

        for i in range(0, len(nums)):
            suffix_sum = nums_sum - prefix_sum - nums[i]
            if suffix_sum == prefix_sum:
                return i
            prefix_sum += nums[i]

        return -1