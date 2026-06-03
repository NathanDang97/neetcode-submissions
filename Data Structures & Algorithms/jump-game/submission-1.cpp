class Solution {
public:
    // greedy solution, O(n) time, O(1) space
    bool canJump(vector<int>& nums) {
        int dest = nums.size() - 1;
        for (int i = nums.size() - 2; i >= 0; i--) {
            if (i + nums[i] >= dest) {
                dest = i;
            }
        }
        return (dest == 0);
    }
};
