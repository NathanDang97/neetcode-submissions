class Solution:
    # backtracking/dfs solution, time O(4^n / sqrt(n))
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        all_possibilities = []

        def backtrack(open_idx, close_idx):
            if open_idx == close_idx == n:
                all_possibilities.append("".join(stack))
                return

            # try the option of opening a paranthesis at the open_idx position
            if open_idx < n:
                stack.append("(")
                backtrack(open_idx + 1, close_idx)
                stack.pop()

            # try closing the corresponding paranthesis if possible
            if close_idx < open_idx:
                stack.append(")")
                backtrack(open_idx, close_idx + 1)
                stack.pop()

        backtrack(0, 0)
        return all_possibilities