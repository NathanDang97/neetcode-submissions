from collections import defaultdict
class Solution:
    # top-down DP solution, O(n) time, O(n) space
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = defaultdict(int)

        def dfs(i):
            if i >= len(cost):
                return 0
            
            if i in cache:
                return cache[i]

            curr_cost = cost[i] + min(dfs(i + 1), dfs(i + 2))
            cache[i] = curr_cost
            return curr_cost

        return min(dfs(0), dfs(1))