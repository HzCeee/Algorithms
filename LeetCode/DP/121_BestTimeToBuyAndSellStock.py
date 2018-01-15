class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[index] denotes the minimum prices in prices[:index+1]
        # dp[index] = min(dp[index - 1], prices[index])
        
        if not prices:
            return 0
        
        minValue = -float("inf")
        dp = [minValue for i in range(len(prices))]
        dp[0] = prices[0]
        maxProfit = 0
        
        for index in range(1, len(dp)):
            dp[index] = min(dp[index - 1], prices[index])
            maxProfit = max(maxProfit, prices[index] - dp[index])
        
        return maxProfit