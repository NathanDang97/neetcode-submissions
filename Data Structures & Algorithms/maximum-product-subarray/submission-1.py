class Solution:
    # Kadane's algorithm, O(n) time, O(1) space
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        curr_max, curr_min = 1, 1

        for num in nums:
            temp = curr_max * num # we want to keep track of the previous curr_max
            # because we modify curr_max here, and we still want to use the previous one to compute curr_min
            curr_max = max(num, num * curr_max, num * curr_min)
            curr_min = min(num, temp, num * curr_min)
            max_product = max(curr_max, max_product)

        return max_product
