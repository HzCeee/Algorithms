class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        
        result = []
        
        for i in range(len(input)):
            if input[i] in '+-*':
                leftCandidate = self.diffWaysToCompute(input[:i])
                rightCandidate = self.diffWaysToCompute(input[i+1:])
                result += [eval(str(left) + input[i] + str(right)) for left in leftCandidate for right in rightCandidate]
        
        return result