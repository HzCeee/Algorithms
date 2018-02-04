class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[i][j] stands for max number of str can we pick from strs with limitation of i "0"s and j "1"s. 
        # For each str, assume it has a "0"s and b "1"s, 
        # we update the dp array iteratively and set dp[i][j] = Math.max(dp[i][j], dp[i - a][j - b] + 1).
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        
        for str in strs:
            count = [0] * 2
            for char in str:
                count[ord(char) - ord('0')] += 1
            for i in range(count[0], m + 1)[::-1]: # reverse so that dp[i][j] only depends on dp[i - count[0]][j - count[1]]
                for j in range(count[1], n + 1)[::-1]:
                    dp[i][j] = max(dp[i][j], dp[i - count[0]][j - count[1]] + 1)
        
        return dp[-1][-1]