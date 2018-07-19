class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        candidates = list(range(1, n+1))
        # return list of all possible combinations of #count numbers out of candidates[leftmostIndex:]
        def combineHelper(leftmostIndex, count):
            if count == 0:
                return [[]]
            res = []
            for numIndex in range(leftmostIndex, n - count + 1):
                for combination in combineHelper(numIndex + 1, count - 1):
                    res.append([candidates[numIndex]] + combination)
            
            return res
        
        return combineHelper(0, k)