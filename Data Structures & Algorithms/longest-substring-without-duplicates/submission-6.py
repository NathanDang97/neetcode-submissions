class Solution:
    # sliding window solution, time O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest = 0
        substring = set()
        l, r = 0, 0

        while r < len(s):
            # move the left pointer if a duplicated character was found
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1

        return longest
