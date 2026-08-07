class Solution {
public:
    // normal sorting solution, O(nlogn) time, O(n) space
    int heightChecker(vector<int>& heights) {
        vector<int> expected = heights;
        sort(expected.begin(), expected.end());

        int diff = 0;
        for (int i = 0; i < heights.size(); i++) {
            if (heights[i] != expected[i]) {
                diff++;
            }
        }
        return diff;
    }
};