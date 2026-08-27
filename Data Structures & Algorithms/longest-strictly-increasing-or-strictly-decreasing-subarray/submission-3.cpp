class Solution {
public:
    // one-pass solution, O(n) time, O(1) space
    int longestMonotonicSubarray(vector<int>& nums) {
        int increase = 1, decrease = 1;
        int longest = 1;

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1]) {
                increase = 1;
                decrease = 1;
            }
            else if (nums[i] > nums[i - 1]) {
                increase++;
                decrease = 1;
            }
            else {
                increase = 1;
                decrease++;
            }
            longest = max(longest, max(increase, decrease));
        }

        return longest;
    }
};