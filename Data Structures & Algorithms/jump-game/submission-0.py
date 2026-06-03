class Solution:
    # greedy solution, O(n) time, O(1) space
    def canJump(self, nums: List[int]) -> bool:
        dest = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= dest:
                dest = i
        
        return dest == 0