class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        leftNum, rightNum = n, n
        
        def generateParenthesisHelper(leftNum, rightNum):
            if leftNum == 0 and rightNum == 0:
                return [""]
            
            res = []
            if leftNum > 0:
                for parenthese in generateParenthesisHelper(leftNum - 1, rightNum):
                    res.append("(" + parenthese)
            if rightNum > leftNum and rightNum > 0:
                for parenthese in generateParenthesisHelper(leftNum, rightNum - 1):
                    res.append(")" + parenthese)
            return res
        
        return generateParenthesisHelper(leftNum, rightNum)