class Solution:
    # sliding window solution, O(n) time, O(1) space since we only consider 26 characters
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = defaultdict(int)
        max_length = 0
        l, r = 0, 0
        while r < len(s):
            frequency[s[r]] += 1

            # move the left pointer and decrement the frequency of s[l]
            # if we do not have enough budget to replace the characters
            while (r - l + 1) - max(frequency.values()) > k:
                frequency[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length