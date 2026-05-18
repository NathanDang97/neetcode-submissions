class Solution:
    # top down DP solution, time O(n + m)
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            cache[(i, j)] = dfs(i, j + 1) + dfs(i + 1, j)
            return cache[(i, j)]

        return dfs(0, 0)