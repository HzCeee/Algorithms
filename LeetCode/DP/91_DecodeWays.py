class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # dp[index] denote the number of ways to decode s[index:]
        # if '09' < s[index: index+2] < '27': dp[index] = dp[index + 2] + dp[index + 1]
        # elif s[index: index+2] >= '27': dp[index] = dp[index + 1]
        # else: dp[index] = 0
        
        if not s:
            return 0
        
        dp = [1 for i in range(len(s) + 1)]
        dp[-2] = 0 if s[-1] == '0' else 1
        
        for index in range(len(s) - 1)[::-1]:
            if '09' < s[index: index+2] < '27':
                dp[index] = dp[index + 2] + dp[index + 1]
            elif s[index: index+2] >= '27':
                dp[index] = dp[index + 1]
            else: 
                dp[index] = 0
        
        return dp[0]