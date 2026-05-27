class Solution {
public:
    // solution using max-heap, O(n) space, O(n + klogn) time
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> max_heap(nums.begin(), nums.end());

        while (k > 1) {
            max_heap.pop();
            k--;
        }

        return max_heap.top();
    }
};
