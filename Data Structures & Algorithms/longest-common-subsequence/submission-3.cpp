class Solution {
public:
    // bottom-up DP solution, O(n * m) time and space
    int longestCommonSubsequence(string text1, string text2) {
        int n = text1.size();
        int m = text2.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1));

        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                // if the characters mismatch, take the max between two options
                // of either skipping the ith char of text1 or skipping the jth char of text2
                if (text1[i] != text2[j]) {
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1]);
                }
                // otherwise, include the matched chatacter in the longest common sequence
                else {
                    dp[i][j] = 1 + dp[i + 1][j + 1];
                }
            }
        }
        
        return dp[0][0];
    }
};
