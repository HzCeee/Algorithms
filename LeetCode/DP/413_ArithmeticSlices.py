class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # dp[index] denotes the number of arithmetic subsequence with A[index] as the ending number
        # dp[index] = dp[index - 1] + 1 if (A[index] - A[index - 1]) == (A[index - 1] - A[index - 2]) else 0
        if not A:
            return 0
        
        dp = [0 for i in range(len(A))]
        count = 0
        
        for index in range(2, len(dp)):
            dp[index] = dp[index - 1] + 1 if (A[index] - A[index - 1]) == (A[index - 1] - A[index - 2]) else 0
            if dp[index] == 0: count += (1 + dp[index - 1]) * dp[index - 1] / 2
        
        count += (1 + dp[-1]) * dp[-1] / 2
        
        return int(count)
        