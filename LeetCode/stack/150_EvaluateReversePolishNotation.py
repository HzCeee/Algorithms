class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        import re
        eleStack = []
        for token in tokens:
            if re.match(r"-?\d+", token):
                nextElement = int(token)
            else:
                num2, num1 = eleStack.pop(), eleStack.pop()
                if token == "+":
                    nextElement = num1 + num2
                elif token == "-":
                    nextElement = num1 - num2
                elif token == "*":
                    nextElement = num1 * num2
                elif token == "/":
                    nextElement = int(num1 / num2)
            eleStack.append(nextElement)
        
        return eleStack[0]