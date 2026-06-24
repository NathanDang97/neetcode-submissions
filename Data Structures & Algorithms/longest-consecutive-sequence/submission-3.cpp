class Solution {
public:
    // brute-force solution, O(n^2) time, O(1) space
    int longestConsecutive(vector<int>& nums) {
        int longest_length = 0;
        unordered_set<int> nums_set(nums.begin(), nums.end());
        
        for (const auto& num : nums) {
            int curr_length = 1;
            while (nums_set.find(num + curr_length) != nums_set.end()) {
                curr_length += 1;
            }
            longest_length = max(longest_length, curr_length);
        }
        return longest_length;
    }
};
