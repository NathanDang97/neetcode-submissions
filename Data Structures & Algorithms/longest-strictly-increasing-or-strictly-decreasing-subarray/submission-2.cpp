class Solution {
public:
    // brute-force solution, O(n^2) time, O(1) space
    int longestMonotonicSubarray(vector<int>& nums) {
        int n = nums.size();
        int longest = 1;

        for (int i = 0; i < n - 1; i++) {
            int currStreak = 1;
            for (int j = i + 1; j < n; j++) {
                if (nums[j] == nums[j - 1] || ((nums[i] < nums[i + 1]) != (nums[j - 1] < nums[j]))) {
                    break;
                }
                currStreak++;
            }
            longest = max(longest, currStreak);
        }
        return longest;
    }
};