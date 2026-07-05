class Solution:
    # brute-force solution, O(n^2) time, O(n) space
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = []

        for i in range(n):
            count = 1
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                count += 1
            if j == n:
                count = 0
            result.append(count)

        return result
