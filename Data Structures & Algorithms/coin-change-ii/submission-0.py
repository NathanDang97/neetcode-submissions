class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(len(dp)):
                diff = i - coin
                if diff >= 0:
                    dp[i] += dp[diff]

        return dp[-1]