class Solution:
    # O(n^2) solution
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)

        for i in range(n):
            curr_prod = 1
            for j in range(n):
                if i != j:
                    curr_prod *= nums[j]

            result.append(curr_prod)

        return result