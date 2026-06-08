class Solution:
    # backtracking solution, O(n!) time, O(n^2) space
    def isSafe(self, r: int, c: int, board: List[List[str]]) -> bool:
        # check if no queen is in the same column above
        curr_row = r - 1
        while curr_row >= 0:
            if board[curr_row][c] == "Q":
                return False
            curr_row -= 1

        # check if no queen is in the upper-left diagonal
        curr_row, curr_col = r - 1, c - 1
        while curr_row >= 0 and curr_col >= 0:
            if board[curr_row][curr_col] == "Q":
                return False
            curr_row -= 1
            curr_col -= 1
        
        # check if no queen is in the upper-right diagonal
        curr_row, curr_col = r - 1, c + 1
        while curr_row >= 0 and curr_col < len(board):
            if board[curr_row][curr_col] == "Q":
                return False
            curr_row -= 1
            curr_col += 1
        
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        all_solutions = []

        def backtrack(r):
            if r == n:
                solution = ["".join(row) for row in board]
                all_solutions.append(solution)
                return

            # for the current row r, try placing a queen in every column c
            for c in range(n):
                if self.isSafe(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "." # backtracking

        backtrack(0)
        return all_solutions