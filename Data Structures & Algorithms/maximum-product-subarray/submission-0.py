class Solution:
    # brute-force solution, O(n^2) time, O(1) space
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]

        for i in range(len(nums)):
            curr_product = nums[i]
            max_product = max(curr_product, max_product)

            for j in range(i + 1, len(nums)):
                curr_product *= nums[j]
                max_product = max(curr_product, max_product)

        return max_product