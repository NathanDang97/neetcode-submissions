class Solution:
    # brute-force solution, O(n^2) time, O(1) space
    def maxArea(self, heights: List[int]) -> int:
        # area = length * height
        max_area = -1
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                curr_length, curr_height = (j - i), min(heights[i], heights[j])
                curr_area = curr_length * curr_height
                max_area = max(max_area, curr_area)

        return max_area