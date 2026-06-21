class Solution:
    # two-pointer solution, O(n) time, O(1) space
    def maxArea(self, heights: List[int]) -> int:
        max_area = -1
        l, r = 0, len(heights) - 1
        while l < r:
            # compute the current area and compare with the max area so far
            curr_height = min(heights[l], heights[r])
            curr_length = r - l
            curr_area = curr_height * curr_length
            max_area = max(max_area, curr_area)

            # move the pointers in a way that maximize the height
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_area