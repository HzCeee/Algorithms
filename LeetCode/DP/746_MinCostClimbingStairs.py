class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # dp[index] denotes the minimum cost including cost[index]
        # dp[index] = min(dp[index - 1], dp[index - 2]) + cost[index]
        
        dp = [0 for index in range(len(cost) + 2)]
        
        for index in range(2, len(dp)):
            dp[index] = min(dp[index - 1], dp[index - 2]) + cost[index - 2]
            
        return min(dp[-1], dp[-2])