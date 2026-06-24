from collections import defaultdict
class Solution:
    # top-down DP solution, O(t * m * n), space O(n)
    # n: length of the string s, m: number of dictionary words, t: max length of the word
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = defaultdict(bool)
        cache[len(s)] = True

        # at every index i, we want to check if the suffix starting at i
        # can be segmented into a valid dicitonary word
        def dfs(i):
            # if we reach the end, then it's a valid segment
            if i == len(s):
                return True

            if i in cache:
                return cache[i]

            # for each word w in wordDict, check if w matches s[i:i + len(w)]
            # recurse to dfs(i + len(w)) and check if it returns True
            for w in wordDict:
                if ((i + len(w)) <= len(s) and s[i:i + len(w)] == w):
                    if dfs(i + len(w)):
                        cache[i] = True
                        return True
                        
            cache[i] = False
            return False

        return dfs(0)
        