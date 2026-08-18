class Solution:
    # brute-force solution, O(m^2 * n^2) time, O(1) space
    # n: number of words, m: length of longest word
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.add(words[i])
                    break

        return list(result)
