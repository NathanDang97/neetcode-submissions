class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = min number of coins that sums to ammount = i
        # initialize all cells to infinite
        dp = [float('inf')] * (amount + 1)
        
        dp[0] = 0
        for i in range(1, len(dp)):
            for coin in coins:
                diff = i - coin
                if diff >= 0:
                    dp[i] = min(dp[i], dp[diff] + 1)

        return dp[amount] if dp[amount] <= amount else - 1