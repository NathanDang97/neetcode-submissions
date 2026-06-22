class Solution {
public:
    // sliding window + frequency counter solution, O(n) time and space
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> frequency;
        for (auto const& c : s) {
            frequency[c] = 0;
        }

        int l = 0, r = 0;
        int longestLength = 0;
        while (r < s.size()) {
            frequency[s[r]]++;
            while (frequency[s[r]] > 1) {
                frequency[s[l]]--;
                l++;
            }
            longestLength = max(longestLength, r - l + 1);
            r++;
        }

        return longestLength;
    }
};
