class Solution:
    # solution using extra O(n) space
    def findDuplicate(self, nums: List[int]) -> int:
        set_nums = set()
        for num in nums:
            if num not in set_nums:
                set_nums.add(num)
            else:
                return num

        return -1
        