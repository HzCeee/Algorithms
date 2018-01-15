class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dp[index] denotes whether s[:index] can be built by wordDict
        # dp[index] = any([dp[i] and s[i: index] in wordDict for i in range(index)])
        
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        
        for index in range(1, len(dp)):
            dp[index] = any(
                [dp[i] and s[i: index] in wordDict for i in range(index)]
            )
        
        return dp[-1]