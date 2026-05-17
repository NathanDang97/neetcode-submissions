class Solution:
    # brute-force solution, time O(n^2)
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[0]

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                result = max(result, curr_sum)

        return result