class Solution:
    # O(n^2) solution
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * len(nums)

        # fill output with prefix products (left to right)
        prefix = 1 # product of all elements left of i
        for i in range(n):
            result[i] *= prefix
            prefix *= nums[i]

        # multiply each index by its suffix product (right to left)
        suffix = 1 # product of all elements right of i
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result