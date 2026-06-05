class Solution:
    # brute-force solution, O(2^n) time and O(n) space (time limit exceeded)
    def lengthOfLIS(self, nums: List[int]) -> int:
        # i: index of the current element
        # j: index of the previous chosen element (initialized to -1)
        def dfs(i, j):
            if i == len(nums):
                return 0

            lis = dfs(i + 1, j) # not include i in the sequence

            if j == -1 or nums[i] > nums[j]:
                lis = max(lis, 1 + dfs(i + 1, i)) # include i in the sequence

            return lis

        return dfs(0, -1)