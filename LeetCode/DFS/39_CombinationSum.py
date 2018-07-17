class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # return list of combinations that sum up to target
        def combinationSumHelper(candidates, target):
            if target == 0:
                return [[]] # note: should be consistent with the definition of output, that is List[List[int]]
            combinationsList = []
            for index, candidate in enumerate(candidates):
                if candidate <= target:
                    for combination in combinationSumHelper(candidates[index:], target - candidate):
                        combinationsList.append([candidate] + combination)
            
            return combinationsList
        
        return combinationSumHelper(sorted(candidates), target)
                        