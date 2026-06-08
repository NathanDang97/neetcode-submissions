class Solution:
    # mathematical solution, time O(n^2), space O(1)
    # simply reverse the matrix and then take the transpose
    def rotate(self, matrix: List[List[int]]) -> None:
        # reverse the matrix vertically
        matrix.reverse()

        # transpose the matrix
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]