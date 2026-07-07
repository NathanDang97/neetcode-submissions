class Solution:
    # bit manipulation solution, O(n) time, O(1) space
    # use XOR (^) to detect the single number
    # if it does not exists, XOR returns 0 as it cancels all the pairs out
    def singleNumber(self, nums: List[int]) -> int:
        is_single = 0
        for num in nums:
            is_single = is_single ^ num
        return is_single