class Solution:
    # bottom-up DP solution, O(n * m * t) time, O(n) space
    # n: length of string s, m: number of words in wordDict, t: length of longest word
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # dp[i] means whether the substring s[i:] can be segmented
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0] 