class Solution:
    # top-down DP solution with hash set, O(t^2 * n + m), space O(n + (m * t))
    # n: length of the string s, m: number of dictionary words, t: max length of the word
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict) # convert to a set for O(1) look up
        t = 0 # length of the longest word in the wordDict
        for w in wordSet:
            t = max(t, len(w))

        cache = defaultdict(bool)
        cache[len(s)] = True

        # at every index i, we want to check if the suffix starting at i
        # can be segmented into a valid dicitonary word.
        # if we can split the string at any valid word boundary and the rest is solvable,
        # then the whole string is solvable.
        def dfs(i):
            # if we reach the end, then it's a valid segment
            if i == len(s):
                return True

            if i in cache:
                return cache[i]

            # for every j from i to len(s) - 1, check if s[i: j + 1] is in the wordSet
            # recurse to dfs(j + 1) and check if it returns True
            # a word can only be as long as the maximum word length in wordDict
            # so we can limit how far we try to split from each index
            for j in range(i, min(len(s), i + t)):
                if s[i:j + 1] in wordSet:
                    if dfs(j + 1):
                        cache[i] = True
                        return True

            cache[i] = False
            return False

        return dfs(0)