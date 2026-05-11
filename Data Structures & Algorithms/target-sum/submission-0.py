class Solution:
    # O(2^n) brute-force solution
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # i = num of elements (in nums) that we looked at
        # curr_sum = the current sum formed by those elements we looked at
        def backtrack(i, curr_sum):
            if i == len(nums):
                return 1 if curr_sum == target else 0

            return backtrack(i + 1, curr_sum + nums[i]) + backtrack(i + 1, curr_sum - nums[i])

        return backtrack(0, 0)