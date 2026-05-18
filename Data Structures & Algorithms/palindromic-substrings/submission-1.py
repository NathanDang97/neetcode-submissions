class Solution:
    # brute-force solution, time O(n^3)
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                if l >= r:
                    count += 1

        return count