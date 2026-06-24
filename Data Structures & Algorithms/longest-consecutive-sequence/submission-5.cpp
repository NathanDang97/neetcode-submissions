class Solution {
public:
    // hasing solution, O(n) time, O(n) space
    int longestConsecutive(vector<int>& nums) {
        int longestLength = 0;
        unordered_set<int> numsSet(nums.begin(), nums.end());

        for (int num : nums) {
            // begin a new sequence with num
            if (numsSet.find(num - 1) == numsSet.end()) {
                int currLength = 1;
                // compute the length of the sequence
                while (numsSet.find(num + currLength) != numsSet.end()) {
                    currLength++;
                }
                // update the max length
                longestLength = max(longestLength, currLength);
            }
        }
        return longestLength;
    }
};
