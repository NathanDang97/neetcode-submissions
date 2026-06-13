class Solution:
    # bottom-up DP solution, O(n^2) time and space
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -2, -1):
                # not including nums[i] in lis
                lis = dp[i + 1][j + 1]
                
                # including nums[i] in lis
                if j == -1 or nums[j] < nums[i]:
                    lis = max(lis, 1 + dp[i + 1][i + 1])
                
                dp[i][j + 1] = lis

        return dp[0][0]