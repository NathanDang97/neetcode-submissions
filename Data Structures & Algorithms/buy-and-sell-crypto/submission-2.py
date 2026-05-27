class Solution:
    # brute force solution, O(n^2) time
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                result = max(result, prices[j] - prices[i])

        return result