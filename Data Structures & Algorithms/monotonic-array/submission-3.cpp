class Solution {
public:
    // one-pass solution, O(n) time, O(1) space
    bool isMonotonic(vector<int>& nums) {
        bool increase = true;
        bool decrease = true;

        for (int i = 0; i < nums.size() - 1; i++) {
            // check for non-decreasing
            if (nums[i] < nums[i + 1]) {
                increase = false;
            }
            // check for non-increasing
            if (nums[i] > nums[i + 1]) {
                decrease = false;
            }
        }

        return increase || decrease;
    }
};