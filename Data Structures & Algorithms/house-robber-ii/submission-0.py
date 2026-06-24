class Solution:
    # the solution to House Robber I problem (where the houses are linearly arranged)
    def rob_helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    # bottom-up DP solution, O(n) time and space
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # use the helper method on nums[1:n-1] and nums[0:n-2]
        # corresponding to the option of skipping the first house or not
        return max(self.rob_helper(nums[1:]), 
                    self.rob_helper(nums[0:n - 1]))
        