class Solution:
    # bottom-up DP solution, O(n^2) time and O(n) space
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            dest = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, dest):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]