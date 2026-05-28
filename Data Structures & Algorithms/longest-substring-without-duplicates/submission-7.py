from collections import defaultdict
class Solution:
    # another sliding window solution using frequency counter
    # O(n) time and space
    def lengthOfLongestSubstring(self, s: str) -> int:
        frequency = defaultdict(int)
        l, r = 0, 0
        longest = 0
        while r < len(s):
            frequency[s[r]] += 1

            while frequency[s[r]] > 1:
                frequency[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
            r += 1

        return longest