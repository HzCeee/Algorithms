class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # dp[num] denotes the least number of perfect square numbers which sum to num.
        # dp[num] = min([dp[num - squareNum] for squareNum in squareNumList])
        dp = [0 for i in range(n + 1)]
        
        for num in range(1, len(dp)):
            dp[num] = 1 + min([dp[num - (i + 1) ** 2] for i in range(int(num ** 0.5))])
            
        return dp[n]