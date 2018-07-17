class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # return the list of combinations that sums up to target:
        def combinationSum2Helper(candidates, target):
            if target == 0:
                return [[]]
            combinationsList = []
            firstNumIndex = 0
            for index, candidate in enumerate(candidates):
                if index > 0 and candidate == candidates[firstNumIndex]:
                    continue
                    
                if index > 0 and candidate != candidates[index - 1]:
                    firstNumIndex = index
                    
                if candidate <= target:
                    for combination in combinationSum2Helper(candidates[index+1:], target - candidate):
                        combinationsList.append([candidate] + combination)
            
            return combinationsList
        
        return combinationSum2Helper(sorted(candidates), target)