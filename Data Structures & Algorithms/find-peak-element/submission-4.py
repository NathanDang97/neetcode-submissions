class Solution:
    # binary search solution, O(log n) time, O(1) space
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            # by always comparing nums[m] with nums[m + 1], we ensure we move toward a peak
            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1

        return r # or return l also works since l == r at this point