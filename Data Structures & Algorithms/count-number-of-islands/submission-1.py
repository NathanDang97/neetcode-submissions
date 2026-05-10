class Solution:
    # BFS solution
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))

            while queue:
                curr_r, curr_c = queue.popleft()
                for dr, dc in directions:
                    new_r = curr_r + dr
                    new_c = curr_c + dc
                    if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols or grid[new_r][new_c] == '0':
                        continue

                    grid[new_r][new_c] = '0'
                    queue.append((new_r, new_c))

        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    bfs(r, c)

        return num_islands