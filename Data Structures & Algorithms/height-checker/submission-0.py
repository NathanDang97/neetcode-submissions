class Solution:
    # sorting solution, O(nlogn) time, O(n) space
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count += 1

        return count

        