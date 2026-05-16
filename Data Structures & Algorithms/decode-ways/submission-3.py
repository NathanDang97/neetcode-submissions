class Solution:
    # top-down dp, time O(n)
    def numDecodings(self, s: str) -> int:
        cache = {len(s) : 1}

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            if i in cache:
                return cache[i]

            num_ways = dfs(i + 1)
            if i < len(s) - 1:
                if s[i] == '1' or (s[i] == '2' and s[i + 1] < '7'):
                    num_ways += dfs(i + 2)

            cache[i] = num_ways
            return num_ways

        return dfs(0)
            