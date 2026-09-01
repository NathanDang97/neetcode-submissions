class Solution {
public:
    // prefix sum solution, O(n) time, O(1) space
    int pivotIndex(vector<int>& nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        int prefixSum = 0;
        for (int i = 0; i < nums.size(); i++) {
            int suffixSum = totalSum - prefixSum - nums[i];
            if (prefixSum == suffixSum) {
                return i;
            }
            prefixSum += nums[i];
        }
        return -1;
    }
};