class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # memo[i][j] denotes the maximum value of score of the first player higher than score of the second player higher given array nums[i: j+1]
        # memo[i, j] = max(nums[i] - memo[i + 1, j], nums[j] - memo[i, j - 1])
        
        self.memo = {}
        
        def predictTheWinnerHelper(numArray, startPtr, endPtr):
            if startPtr == endPtr:
                return numArray[startPtr]
            
            if (startPtr, endPtr) in self.memo:
                return self.memo[(startPtr, endPtr)]
            
            self.memo[(startPtr, endPtr)] = max(
                nums[startPtr] - predictTheWinnerHelper(numArray, startPtr + 1, endPtr),
                nums[endPtr] - predictTheWinnerHelper(numArray, startPtr, endPtr - 1)
            )
            
            return self.memo[(startPtr, endPtr)]
        
        return predictTheWinnerHelper(nums, 0, len(nums) - 1) >= 0