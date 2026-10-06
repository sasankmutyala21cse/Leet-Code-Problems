class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], 1 + dp[j - coin])

        return -1 if dp[amount] == float('inf') else dp[amount]