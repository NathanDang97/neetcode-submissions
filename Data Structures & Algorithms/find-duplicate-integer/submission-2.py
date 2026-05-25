class Solution:
    # solution with no extra space, i.e. O(1) space
    # the idea is to treat the array like a linked list
    # that is, have the index i points to nums[i]
    # eventually, we will find some indices j, k where nums[j] = nums[k]
    def findDuplicate(self, nums: List[int]) -> int:
        # use Floyd's algorithm detecting a cycle and the start of the cycle
        # Phase 1: detect the cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break 

        # Phase 2: detect the starting point of the cycle
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast # or return slow, both work