class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        numStack = []
        operator, num = None, 0
        for index, char in enumerate(s):
            if char.isdigit():
                num = 10 * num + int(char)
            if (not char.isdigit() and not char.isspace()) or index == len(s) - 1:
                if operator:
                    if operator == "+":
                        numStack.append(num)
                    elif operator == "-":
                        numStack.append(-num)
                    elif operator == "*":
                        numStack.append(numStack.pop() * num)
                    elif operator == "/":
                        leftNum = numStack.pop()
                        numStack.append(abs(leftNum) // num * (1 if leftNum >= 0 else -1))
                else:
                    numStack.append(num)
                num = 0
                operator = char
        return sum(numStack)