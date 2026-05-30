class Solution:
    # binary search solution, O(log n) time
    # idea: the minimum is the rotated point of the array
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            # search the right half for the minimum
            if nums[m] > nums[r]:
                l = m + 1
            # search the left half for the minimum
            else:
                r = m

        return nums[l]