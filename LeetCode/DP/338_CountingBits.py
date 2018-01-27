class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # dp[i] denotes the number of 1's of i's binary representation
        # dp[i] = dp[i - offset] + 1 where offset is the closest number with power of 2. e.g. for number 7, it is offset is 4
        
        dp = [0 for i in range(num + 1)]
        offset = 1
        for i in range(1, len(dp)):
            if i >> 1 == offset:
                offset <<= 1
            dp[i] = dp[i - offset] + 1
            
        return dp