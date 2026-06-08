class Solution:
    # brute-force solution, time and space O(n^2)
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]

        # rotated position of matrix[i][j] is given by matrix[j][n - 1 - i]
        for i in range(n):
            for j in range(n):
                rotated[j][n - 1 - i] = matrix[i][j]

        # copy the values of the rotated matrix to the original matrix
        for i in range(n):
            for j in range(n):
                matrix[i][j] = rotated[i][j]