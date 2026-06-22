class Solution:
    # brute-force solution, O(n^2) time, O(1) space
    def trap(self, height: List[int]) -> int:
        # for each position, the water trapped above it depends on
        # the tallest bar to its left and the tallest bar to its right
        # given these two values, the water trapped at index i is:
        # min(left_max, right_max) - height[i]
        if not height:
            return 0
        trapped_water = 0
        n = len(height)

        for i in range(n):
            max_left, max_right = height[i], height[i]

            for j in range(i):
                max_left = max(max_left, height[j])
            for j in range(i + 1, n):
                max_right = max(max_right, height[j])

            trapped_water += min(max_left, max_right) - height[i]

        return trapped_water