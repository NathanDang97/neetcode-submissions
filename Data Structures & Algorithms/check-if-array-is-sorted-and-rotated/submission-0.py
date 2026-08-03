class Solution:
    # iteration solution, check for the unique rotated point
    # if the array was sorted and then rotated, there can only be one rotated point
    # O(n) time, O(1) space
    def check(self, nums: List[int]) -> bool:
        count, n = 0, len(nums)
        for i in range(n):
            # use modulo n for wrap around
            if nums[i] > nums[(i + 1) % n]:
                count += 1
            if count > 1:
                return False

        return True