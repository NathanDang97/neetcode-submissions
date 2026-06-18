class Solution {
public:
    // hash-map solution, O(n) time and space
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> residues; // maps the value to its index in nums
        for (int i = 0; i < nums.size(); i++) {
            // check if the complement already exists in the hasp map
            // if so, return the incides of the current element and its complement
            int diff = target - nums[i];
            if (residues.find(diff) != residues.end()) {
                int j = residues[diff];
                return {j, i};
            }
            else {
                residues[nums[i]] = i;
            }
        }
        return {-1, -1};
    }
};
