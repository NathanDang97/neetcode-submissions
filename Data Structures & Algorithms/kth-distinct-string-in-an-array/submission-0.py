class Solution:
    # frequency counter solution, O(n) time and space
    def kthDistinct(self, arr: List[str], k: int) -> str:
        frequency = defaultdict(int)
        for s in arr:
            frequency[s] += 1
        
        for s, c in frequency.items():
            if c == 1:
                k -= 1
            if k == 0:
                return s

        return ""