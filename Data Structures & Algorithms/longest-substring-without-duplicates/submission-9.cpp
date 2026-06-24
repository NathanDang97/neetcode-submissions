class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0, r = 0;
        int longest = 0;
        unordered_set<char> subString;
        while (r < s.size()) {
            // move the left pointer if a duplicated character was found
            while (subString.find(s[r]) != subString.end()) {
                subString.erase(s[l]);
                l++;
            }
            subString.insert(s[r]);
            longest = max(longest, r - l + 1);
            r++;
        }
        return longest;
    }
};
