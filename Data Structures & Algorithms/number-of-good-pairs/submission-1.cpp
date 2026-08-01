class Solution {
public:
    // frequency counter solution, O(n) time and space
    int numIdenticalPairs(vector<int>& nums) {
        unordered_map<int, int> counter;
        int numPairs = 0;
        for (int num : nums) {
            numPairs += counter[num];
            counter[num]++;
        }
        return numPairs;
    }
};