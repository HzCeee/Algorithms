class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        # dp[index] denotes the number of substrings of p in the string s which ends with p[index]
        # dp[index] = 
        # dp[index - 1] + 1 if (ord(p[index]) - ord(p[index - 1])) == 1 or (ord(p[index - 1]) - ord(p[index]) == 25) else 1
        
        if not p:
            return 0
        
        dp = [1 for i in range(len(p))]
        count = {chr(char):0 for char in range(ord('a'), ord('z') + 1)}
        count[p[0]] = 1
        for index in range(1, len(dp)):
            dp[index] = dp[index - 1] + 1 if (ord(p[index]) - ord(p[index - 1])) == 1 or (ord(p[index - 1]) - ord(p[index]) == 25) else 1
            count[p[index]] = max(dp[index], count[p[index]])
        
        return sum(count.values())