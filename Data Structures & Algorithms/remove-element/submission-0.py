class Solution:
    # use two pointers to remove elements in place without extra space
    # O(n) time, O(1) space
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k