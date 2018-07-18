class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = 24
        self.memo = {}
        # return if we can find such equation which equals target
        def judgePoint24Helper(candidates):
            if len(candidates) == 1:
                return abs(candidates[0] - target) < 0.00001
            
            for num1Index in range(len(candidates) - 1):
                for num2Index in range(num1Index + 1, len(candidates)):
                    for operator in ["+", "-", "*", "/"]:
                        candidatePool = set()
                        num1, num2 = candidates[num1Index], candidates[num2Index]
                        if tuple(sorted([num1, num2]) + [operator]) in self.memo:
                            candidatePool = self.memo[tuple(sorted([num1, num2]) + [operator])]
                        else:
                            for leftNum, rightNum in [(num1, num2), (num2, num1)]:
                                if operator == "/" and rightNum == 0:
                                    continue
                                candidatePool.add(eval(str(leftNum) + operator + str(rightNum)))
                            self.memo[tuple(sorted([num1, num2]) + [operator])] = candidatePool
                        
                        leftCandidates = candidates[:num1Index] + candidates[num1Index + 1: num2Index] + candidates[num2Index + 1:]
                        for newCandidates in candidatePool:
                            if judgePoint24Helper(leftCandidates + [newCandidates]):
                                return True
            
            return False
        
        return judgePoint24Helper(nums)