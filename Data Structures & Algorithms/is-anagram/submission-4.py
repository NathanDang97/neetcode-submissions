class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        frequency = defaultdict(int)
        for c in s:
            frequency[c] += 1

        for c in t:
            if c in frequency:
                frequency[c] -= 1
                if frequency[c] < 0:
                    return False
            else:
                return False

        return True