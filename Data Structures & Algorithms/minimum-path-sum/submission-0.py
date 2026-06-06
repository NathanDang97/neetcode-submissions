from collections import defaultdict
class Solution:
    # top-down DP solution, O(m * n) time and space
    def minPathSum(self, grid: List[List[int]]) -> int:
        min_sum = 0
        cache = defaultdict(int)
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]

            if r == rows or c == cols:
                return float('inf')

            if (r, c) in cache:
                return cache[(r, c)]

            curr_sum = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            cache[(r, c)] = curr_sum
            return curr_sum

        return dfs(0, 0)