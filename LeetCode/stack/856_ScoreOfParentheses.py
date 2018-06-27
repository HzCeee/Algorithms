class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for char in S:
            if char == "(":
                stack.append(char)
            else:
                curElem = stack.pop()
                valueBetweenParentheses = 0
                while curElem != "(":
                    if curElem.isdigit():
                        valueBetweenParentheses += int(curElem)
                    curElem = stack.pop()
                stack.append(str(1) if valueBetweenParentheses == 0 else str(2*valueBetweenParentheses))
                
        return sum(map(lambda x: int(x), stack))
                
                    