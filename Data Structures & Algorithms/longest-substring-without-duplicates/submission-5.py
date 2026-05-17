class Solution:
    # brute-force solution, time O(n^2)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest = 0
        for i in range(len(s)):
            substring = set()
            for j in range(i, len(s)):            
                if s[j] in substring:
                    break
                substring.add(s[j])
            longest = max(longest, len(substring))

        return longest
