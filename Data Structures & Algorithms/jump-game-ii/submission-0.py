class Solution:
    # greedy solution (two-pointer), O(n) time and O(1) space
    def jump(self, nums: List[int]) -> int:
        num_jumps = 0
        l, r = 0, 0
        
        while r < len(nums) - 1:
            furthest_jump = 0
            # compute the furthest jump we can make in the range [l, r]
            for i in range(l, r + 1):
                furthest_jump = max(furthest_jump, i + nums[i])
            # update the next range and increment the number of jumps
            l = r + 1
            r = furthest_jump
            num_jumps += 1

        return num_jumps