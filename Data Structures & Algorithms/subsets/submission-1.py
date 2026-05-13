class Solution:
    # backtracking (dfs) solution, O(n * 2^n) time
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []

        def backtrack(i, subset):
            if i >= len(nums):
                all_subsets.append(subset[:])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            backtrack(i + 1, subset)

        backtrack(0, [])

        return list(all_subsets)