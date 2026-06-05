class Solution:
    # top-down DP solution, O(n * m) time and space
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        cache = [[-1] * n for _ in range(m)]

        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            if r >= m or c >= n or obstacleGrid[r][c] == 1:
                return 0
            
            if cache[r][c] != -1:
                return cache[r][c]

            steps = dfs(r + 1, c) + dfs(r, c + 1)
            cache[r][c] = steps
            return steps

        return dfs(0, 0)
            