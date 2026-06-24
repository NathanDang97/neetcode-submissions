class Solution {
public:
    // solution using hashmap + sorting, O(m * nlogn) time, O(m * n) space
    // m: the number of strings, n: the length of the longest string
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramsMap;
        for (string s : strs) {
            string sortedS = s;
            sort(sortedS.begin(), sortedS.end());
            anagramsMap[sortedS].push_back(s);
        }
        vector<vector<string>> anagramsList;
        for (const auto& pair : anagramsMap) {
            anagramsList.push_back(pair.second);
        }
        return anagramsList;
    }
};
