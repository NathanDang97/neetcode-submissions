from collections import defaultdict
class Solution:
    # hash-map solution, O(n) time, O(m) space
    # n: length of string, m: number of unique characters
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = defaultdict(str) # maps char s[i] to t[i]
        t_to_s = defaultdict(str) # maps char t[i] to s[i]

        for i in range(len(s)):
            if (s[i] in s_to_t and s_to_t[s[i]] != t[i]) \
                or (t[i] in t_to_s and t_to_s[t[i]] != s[i]):
                return False
            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i] 

        return True