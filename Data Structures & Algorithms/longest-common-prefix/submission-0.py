class Solution:
    # O(n * mlogm) time, n: the length of the longest string, m: the number of strings
    # O(1) or O(m) space depending on the sorting algorithm
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort the strings, then the lcp is defined by
        # the common substring between the smallest and largest string
        strs.sort()
        first, last = strs[0], strs[-1]

        i = 0
        while i < min(len(first), len(last)) and first[i] == last[i]:
            i += 1

        return first[:i]  