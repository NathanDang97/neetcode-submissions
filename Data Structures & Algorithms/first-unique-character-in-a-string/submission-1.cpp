class Solution {
public:
    // two-pass solution with frequency counter, O(n) time and space
    int firstUniqChar(string s) {
        unordered_map<char, int> frequency;
        for (const auto& c : s) {
            frequency[c]++;
        }

        for (int i = 0; i < s.size(); i++) {
            if (frequency[s[i]] == 1) {
                return i;
            }
        }

        return -1;
    }
};