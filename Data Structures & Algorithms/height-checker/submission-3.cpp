class Solution {
public:
    // counting sort solution, O(n + k) time and space
    int heightChecker(vector<int>& heights) {
        int heightCount[101] = {};
        for (int h : heights) {
            heightCount[h]++;
        }

        vector<int> expected;
        for (int h = 1; h <= 100; h++) {
            int currCount = heightCount[h];
            while (currCount > 0) {
                expected.push_back(h);
                currCount--;
            }
        }

        int diff = 0;
        for (int i = 0; i < heights.size(); i++) {
            if (heights[i] != expected[i]) {
                diff++;
            }
        }
        return diff;
    }
};