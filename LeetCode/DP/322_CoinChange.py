class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[num] denotes the fewest number of coins needed to make up num
        # dp[num] = min([dp[num - coin] for coin in coins if coin <= num]) + 1
        
        dp = [0 for i in range(amount + 1)]
        
        for num in range(1, len(dp)):
            candidate = [dp[num - coin] for coin in coins if coin <= num]
            dp[num] = min(candidate) + 1 if candidate else float('inf')
        
        return dp[amount] if dp[amount] < float('inf') else -1