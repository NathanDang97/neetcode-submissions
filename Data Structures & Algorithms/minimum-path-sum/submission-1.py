class Solution:
    # bottom-up DP solution, O(m * n) time and space
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]
        dp[rows - 1][cols] = 0
        dp[rows][cols - 1] = 0

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0] 