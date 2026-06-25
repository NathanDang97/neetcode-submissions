class Solution:
    # one-pass binary search solution, O(log n) time, O(1) space
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            
            # if we are at the left sorted portion
            if nums[m] >= nums[l]:
                # do regular binary search inside this portion
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # if we are at the right sorted portion
            else:
                # do regular binary search inside this portion
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
