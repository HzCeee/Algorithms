class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i][j] refers to the longest palindromic subsequence's length in s[i: j + 1]
        # if s[i] == s[j]: dp[i][j] = dp[i + 1][j - 1] + 2
        # else: dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        dp = [[1 if i == j else 0 for j in range(len(s))] for i in range(len(s))]
        
        for i in range(len(s))[::-1]:
            for j in range(i + 1, len(s)):
                dp[i][j] = dp[i + 1][j - 1] + 2 if s[i] == s[j] else max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][-1]