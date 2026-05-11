class Solution:
    # O(n * m) top-down dp solution, m: the sum of all elements in nums
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # dp[(i, curr_sum)]: the number of ways to form curr_sum starting from index i

        def backtrack(i, curr_sum):
            if i == len(nums):
                return 1 if curr_sum == target else 0

            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]

            dp[(i, curr_sum)] = backtrack(i + 1, curr_sum + nums[i]) + backtrack(i + 1, curr_sum - nums[i])

            return dp[(i, curr_sum)]

        return backtrack(0, 0)