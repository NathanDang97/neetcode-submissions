class Solution:
    # iterative solution, O(n * 2^n) time
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = [[]]

        for num in nums:
            all_subsets += [subset + [num] for subset in all_subsets]

        return all_subsets