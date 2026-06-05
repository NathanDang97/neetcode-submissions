class Solution:
    # top-down DP solution, O(n^2) time and O(n^2) space
    # 2D-DP approach
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # i: index of the current element
        # j: index of the previous chosen element (initialized to -1)
        # offset j's by 1 since j can range from -1 to n - 1
        cache = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, j):
            if i == len(nums):
                return 0

            if cache[i][j + 1] != -1:
                return cache[i][j + 1]

            lis = dfs(i + 1, j) # not include i in the sequence

            if j == -1 or nums[i] > nums[j]:
                lis = max(lis, 1 + dfs(i + 1, i)) # include i in the sequence

            cache[i][j + 1] = lis
            return lis

        return dfs(0, -1)