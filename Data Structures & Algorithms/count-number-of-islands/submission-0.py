class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # idea: use DFS and mark the tiles as we go
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return

            grid[r][c] = '0'
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        num_of_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_of_islands += 1
                    dfs(r, c)

        return num_of_islands