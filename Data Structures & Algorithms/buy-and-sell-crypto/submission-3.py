class Solution:
    # sliding window solution, O(n) time
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                result = max(result, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return result