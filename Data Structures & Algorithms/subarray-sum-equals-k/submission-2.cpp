class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        // maps a prefix sum to its frequency
        unordered_map<int, int> prefixSums;
        prefixSums[0] = 1;
        int count = 0, currSum = 0;

        // let prefix_sum[i] denotes a prefix sum up to index i
        // then if some prefix_sum[j] - prefix_sum[i] = k,
        // it means the subarray from index i + i to j has sum k
        for (int i = 0; i < nums.size(); i++) {
            // compute the prefix sum up to index i
            currSum += nums[i];

            // check if a prefix sum of (currSum - k) already presents
            int diff = currSum - k;
            count += prefixSums[diff];

            // increase the frequency of the current prefix sum
            prefixSums[currSum]++;
        }
        return count;
    }
};