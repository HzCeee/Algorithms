class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # dp[num] denotes the number of structurally unique BST's that store values from 1 to num
        # dp[num] = (dp[0] * dp[num - 1]) + (dp[1] * dp[num - 2]) + ... + (dp[num - 1] * dp[0])
        # for example, dp[i] * dp[num - 1 - i] means the number of structurally unique BST's with root value i
        
        dp = [1 for i in range(n + 1)]
        
        for num in range(2, n + 1):
            uniqueBst = 0
            for i in range(1, num + 1):
                uniqueBst += dp[i - 1] * dp[num - i]
            dp[num] = uniqueBst
                
        return dp[n]