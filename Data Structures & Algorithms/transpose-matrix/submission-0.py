class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        transpose = [[0] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                transpose[c][r] = matrix[r][c]

        return transpose