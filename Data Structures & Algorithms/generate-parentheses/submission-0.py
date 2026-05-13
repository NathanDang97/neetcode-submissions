class Solution:
    # brute-force solution, time O(n * 4^n)
    def generateParenthesis(self, n: int) -> List[str]:
        
        def valid_parenthesis(s):
            count = 0

            for c in s:
                if c == ')':
                    count -= 1
                    if count < 0:
                        return False
                
                else:
                    count += 1

            return count == 0

        all_parentheses = []

        def dfs(s):
            if len(s) == n * 2:
                if valid_parenthesis(s):
                    all_parentheses.append(s)
                return

            dfs(s + '(')
            dfs(s + ')')

        dfs('')
        return all_parentheses
            


