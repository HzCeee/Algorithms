class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # free[i] denotes the max profit on day[i] with no stock in hand
        # hold[i] denotes the max profit on day[i] with stock in hand
        # coolDown[i] denotes the max profit on day[i] in coolDown state
        #
        # free[i] = max(free[i - 1], coolDown[i - 1])
        # hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
        # coolDown[i] = hold[i - 1] + prices[i]
        
        if not prices:
            return 0
        
        free, hold, coolDown = [0 for i in range(len(prices))], [0 for i in range(len(prices))], [0 for i in range(len(prices))]
        free[0], hold[0], coolDown[0] = 0, -prices[0], 0
        
        for i in range(1, len(prices)):
            free[i] = max(free[i - 1], coolDown[i - 1])
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            coolDown[i] = hold[i - 1] + prices[i]
            
        return max(free[-1], coolDown[-1])