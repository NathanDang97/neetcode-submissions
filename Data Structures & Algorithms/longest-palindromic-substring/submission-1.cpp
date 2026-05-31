class Solution {
public:
    // two-pointer solution, O(n^2) time, O(1) space
    string longestPalindrome(string s) {
        int startIdx = 0; // start index of the longest palindrome
        int maxLength = 0; // the length of the longest palindrome

        for (int i = 0; i < s.size(); i++) {
            // even palindrome
            int l = i;
            int r = i;
            while (l >= 0 && r < s.size() && s[l] == s[r]) {
                if (r - l + 1 > maxLength) {
                    maxLength = r - l + 1;
                    startIdx = l;
                }
                l--;
                r++;
            }

            // odd palindrome
            l = i;
            r = i + 1;
            while (l >= 0 && r < s.size() && s[l] == s[r]) {
                if (r - l + 1 > maxLength) {
                    maxLength = r - l + 1;
                    startIdx = l;
                }
                l--;
                r++;
            }
        }
        return s.substr(startIdx, maxLength);
    }
};
