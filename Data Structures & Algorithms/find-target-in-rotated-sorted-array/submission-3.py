class Solution:
    # binary search solution (2 passes), O(log n) time, O(1) space
    def search(self, nums: List[int], target: int) -> int:
        # pass 1: find the rotated point which is also the minimum
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m # the rotated point might be nums[m]

        # determine which half the target number should belong to
        pivot = l
        l, r = 0, len(nums) - 1
        if nums[pivot] <= target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        # pass 2: regular binary search to find the target number in the designated half
        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        return -1