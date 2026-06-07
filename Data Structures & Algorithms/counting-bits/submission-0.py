class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            count = 0
            while i > 0:
                count += (i & 1)
                i = i >> 1
            result.append(count)
        return result