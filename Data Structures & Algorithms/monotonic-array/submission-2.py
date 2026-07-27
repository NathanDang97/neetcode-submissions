class Solution:
    # one-pass solution, O(n) time, O(1) space
    def isMonotonic(self, nums: List[int]) -> bool:
        increase, decrease = True, True

        for i in range(len(nums) - 1):
            # check for non-decreasing
            if nums[i] < nums[i + 1]:
                decrease = False
            # check for non-increasing
            if nums[i] > nums[i + 1]:
                increase = False

        # if the given array is monotonic, one of the flags is true
        return increase or decrease