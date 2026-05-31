class Solution:
    # two-pointer solution, time O(n^2), space O(1)
    def longestPalindrome(self, s: str) -> str:
        start_idx = 0 # the start index of the longest palindrome
        longest_len = 0 # the length of the longest palindrome

        # compute the longest palindrome at each index i as the center
        for i in range(len(s)):
            # even palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest_len:
                    start_idx = l
                    longest_len = r - l + 1
                l -= 1
                r += 1

            # odd palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest_len:
                    start_idx = l
                    longest_len = r - l + 1
                l -= 1
                r += 1

        return s[start_idx : start_idx + longest_len]