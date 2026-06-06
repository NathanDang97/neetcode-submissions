class Solution:
    # bottom-up DP solution, O(n) time and O(1) space
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # rob1: best value up to the (i-2)-th house
        # rob2: best value up to the (i-1)-th house
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2