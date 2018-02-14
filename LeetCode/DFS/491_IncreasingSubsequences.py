class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.memo = {}
        
        # return the all the different possible increasing subsequences of nums
        # with format [[subs1], [subs2], ..., [subsn]]
        def findSubsequencesHelper(nums):
            if str(nums) in self.memo:
                return self.memo[str(nums)]
            
            if len(nums) == 1:
                self.memo[str(nums)] = [[nums[0]]]
                return self.memo[str(nums)]
            
            startNumber = nums[0]
            self.memo[str(nums)] = [[startNumber]]
            
            subsequencesList = findSubsequencesHelper(nums[1:])
            
            for subsequece in subsequencesList:
                if startNumber <= subsequece[0]:
                    if [startNumber] + subsequece not in self.memo[str(nums)]:
                        self.memo[str(nums)].append([startNumber] + subsequece)
                self.memo[str(nums)].append(subsequece)
            
            return self.memo[str(nums)]
        
        sequenceList = findSubsequencesHelper(nums)
        result = [sequence for sequence in sequenceList if len(sequence) >= 2]
        
        return result