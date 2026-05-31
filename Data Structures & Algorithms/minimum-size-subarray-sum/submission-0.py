class Solution:
    # brute-force solution, O(n^2) time, O(1) space
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_length = float('inf')

        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum >= target:
                    min_length = min(min_length, j - i + 1)
                    break

        return min_length if min_length != float('inf') else 0