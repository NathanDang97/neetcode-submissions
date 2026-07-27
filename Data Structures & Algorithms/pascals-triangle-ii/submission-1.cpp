class Solution {
public:
    // top-down DP, O(n^2) time, O(n) space
    vector<int> getRow(int rowIndex) {
        if (rowIndex == 0) {
            return {1};
        }

        vector<int> currRow = {1};
        vector<int> prevRow = getRow(rowIndex - 1);

        for (int i = 1; i < rowIndex; i++) {
            currRow.push_back(prevRow[i] + prevRow[i - 1]);
        }

        currRow.push_back(1);
        return currRow;
    }
};