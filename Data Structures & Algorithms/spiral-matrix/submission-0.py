class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        # x corresponds to the cols (i.e. moving horizontally)
        # y corresponds to the rows (i.e. moving vertically)
        x, y, dx, dy = 0, 0, 1, 0
        spiral_order = []

        for _ in range(rows * cols):
            spiral_order.append(matrix[y][x])
            matrix[y][x] = '@' # mark as visited
            new_x = x + dx
            new_y = y + dy
            # check if reached boundaries or if reached a visited cell
            if new_x < 0 or new_x >= cols or new_y < 0 or new_y >= rows \
                or matrix[new_y][new_x] == '@':
                dx, dy = -dy, dx
            # update the coordinate
            x += dx
            y += dy

        return spiral_order
            