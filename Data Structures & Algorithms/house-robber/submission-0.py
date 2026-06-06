class Solution:
    # top-down DP solution, O(n) time and space
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n
        
        def dfs(i):
            if i >= n:
                return 0
            if cache[i] != -1:
                return cache[i]

            # take the max of one of the two options
            # either rob the current ith house and skip the (i+1)-th
            # or skip the ith house and rob the (i+1)-th
            rob = max(dfs(i + 1), nums[i] + dfs(i + 2))
            cache[i] = rob
            return rob

        return dfs(0)