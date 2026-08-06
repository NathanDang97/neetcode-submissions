class Solution:
    # counting sort solution, O(n + k) time and space
    def heightChecker(self, heights: List[int]) -> int:
        height_count = [0] * 101
        for height in heights:
            height_count[height] += 1

        expected = []
        for height, count in enumerate(height_count):
            while count > 0:
                expected.append(height)
                count -= 1

        diff = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                diff += 1

        return diff
