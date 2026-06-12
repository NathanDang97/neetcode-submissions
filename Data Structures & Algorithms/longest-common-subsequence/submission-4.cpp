class Solution {
private:
    vector<vector<int>> cache;
    
    int dfs(string text1, string text2, int i, int j) {
        if (i == text1.size() || j == text2.size()) {
            return 0;
        }
        if (cache[i][j] != - 1) {
            return cache[i][j];
        }

        int curr_lcs_length;
        // if the characters mismatch, try both options
        // skipping text1[i] or skipping text2[j]
        if (text1[i] != text2[j]) {
            curr_lcs_length = max(dfs(text1, text2, i + 1, j), dfs(text1, text2, i, j + 1));
        }
        // otherwise, include the mathced chatacter to the lcs
        else {
            curr_lcs_length = 1 + dfs(text1, text2, i + 1, j + 1);
        }

        cache[i][j] = curr_lcs_length; // save the current result
        return curr_lcs_length;
    }

public:
    // top-down DP solution, O(n * m) time and space
    int longestCommonSubsequence(string text1, string text2) {
        int n = text1.size();
        int m = text2.size();
        cache.assign(n, vector<int>(m, -1));
        return dfs(text1, text2, 0, 0);
    }
};
