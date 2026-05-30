class Solution {
public:
    // binary search solution, O(log n) time, O(1) space
    int findMin(vector<int> &nums) {
        int l = 0;
        int r = nums.size() - 1;
        while (l < r) {
            int m = l + (r - l) / 2;
            // search the right half for the minimum
            // i.e. adjust the left pointer
            if (nums[m] > nums[r]) {
                l = m + 1;
            }
            // search the left half (including the mid) for the minimum
            // i.e. adjust the right pointer
            else {
                r = m; // note: do not exclude the mid element
            }
        }
        return nums[l];
    }
};
