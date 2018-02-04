class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        # memo denotes whether 
        # the curren player can win given the candidate number and desired total number
        
        if (1 + maxChoosableInteger) * maxChoosableInteger/2 < desiredTotal:
            return False
        self.memo = {}
        
        def canIWinHelper(nums, desiredTotal):
            hashKey = str(nums)
            if hashKey in self.memo:
                return self.memo[hashKey]

            if nums[-1] >= desiredTotal:
                return True

            for i in range(len(nums)):
                if not canIWinHelper(nums[:i] + nums[i+1:], desiredTotal - nums[i]):
                    self.memo[hashKey]= True
                    return True
            self.memo[hashKey] = False
            return False
        
        return canIWinHelper(list(range(1, maxChoosableInteger + 1)), desiredTotal)