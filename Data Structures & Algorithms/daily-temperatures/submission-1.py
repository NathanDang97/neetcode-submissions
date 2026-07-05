class Solution:
    # monotonic stack solution, O(n) time and space
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and temperatures[i] > stack[-1][0]:
                _, idx = stack.pop()
                result[idx] = i - idx
            stack.append((t, i))

        return result