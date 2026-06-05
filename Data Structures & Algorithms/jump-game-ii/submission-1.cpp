class Solution {
public:
    // greedy (two-pointer) solution, O(n) time and O(1) space 
    int jump(vector<int>& nums) {
        int numJumps = 0;
        int l = 0, r = 0;
        while (r < nums.size() - 1) {
            // compute the furthest jump we can make in range [l, r]
            int furthestJump = 0;
            for (int i = l; i < r + 1; i++) {
                furthestJump = max(furthestJump, i + nums[i]);
            }
            // update the next range and increment the jump counter
            l = r + 1;
            r = furthestJump;
            numJumps++;
        }
        return numJumps;
    }
};
