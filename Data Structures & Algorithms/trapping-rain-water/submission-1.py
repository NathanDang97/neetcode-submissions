class Solution:
    # two-pointer solution, O(n) time, O(1) space
    def trap(self, height: List[int]) -> int:
        # for each position, the water trapped above it depends on
        # the tallest bar to its left and the tallest bar to its right
        # given these two values, the water trapped at index i is:
        # min(max_left, max_right) - height[i]
        if not height:
            return 0
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        trapped_water = 0
        while l < r:
            # if min(max_left, max_right) = max_left
            # we calculate the water trapped at the left pointer l
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                trapped_water += max_left - height[l]

            # if min(max_left, max_right) = max_right
            # we calculate the water trapped at the left pointer r
            else:
                r -= 1
                max_right = max(max_right, height[r])
                trapped_water += max_right - height[r]

        return trapped_water
        
