class Solution:
    # top-down DP solution, time O(n * m), space O(n * m)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        cache = [[-1] * l2 for _ in range(l1)]

        def dfs(i, j):
            if i == l1 or j == l2:
                return 0

            if cache[i][j] != -1:
                return cache[i][j]
            
            if text1[i] == text2[j]:
                curr_length = 1 + dfs(i + 1, j + 1)
            else: 
                curr_length = max(dfs(i + 1, j), dfs(i, j + 1))

            cache[i][j] = curr_length
            return curr_length

        return dfs(0, 0)