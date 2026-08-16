class Solution {
public:
    // suffix max solution, O(n) time, O(1) space (does not count the output space)
    vector<int> replaceElements(vector<int>& arr) {
        int rightMax = -1;
        vector<int> result(arr.size());
        for (int i = arr.size() - 1; i >= 0; i--) {
            result[i] = rightMax;
            rightMax = max(rightMax, arr[i]);
        }
        return result;
    }
};