class Solution:
    # binary search solution, time O(log n + log m)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # first binary search pass: find the row where the target belongs to
        top_row, bot_row = 0, rows - 1
        while top_row <= bot_row:
            mid_row = top_row + (bot_row - top_row) // 2
            if target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot_row = mid_row - 1
            else:
                break

        # second binary search pass: find the target in this particular row
        if not (top_row <= bot_row):
            return False
        # the row where the target should be
        row = top_row + (bot_row - top_row) // 2
        left_col, right_col = 0, cols - 1
        while left_col <= right_col:
            mid_col = left_col + (right_col - left_col) // 2
            if target > matrix[row][mid_col]:
                left_col = mid_col + 1
            elif target < matrix[row][mid_col]:
                right_col = mid_col - 1
            else:
                return True

        return False