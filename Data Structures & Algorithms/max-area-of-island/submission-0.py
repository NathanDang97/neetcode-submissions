class Solution:
    # bfs solution, time and space O(rows * cols)
    def maxAreaOfIsland(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def bfs(r : int, c : int) -> int:
            queue = deque()
            queue.append((r, c))
            matrix[r][c] = 0
            size = 1
            
            while queue:
                curr_row, curr_col = queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = curr_row + dr, curr_col + dc
                    if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] == 1:
                        size += 1
                        matrix[new_row][new_col] = 0
                        queue.append((new_row, new_col))
                        
            return size
        
        max_size = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    curr_size = bfs(r, c)
                    max_size = max(max_size, curr_size)
                    
        return max_size