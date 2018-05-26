class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                charBuffer = []
                numBuffer = []
                finishReadChar = False
                
                while True:
                    if not stack: break
                    token = stack.pop()
                    
                    if finishReadChar and (token.isalpha() or token == "["):
                        stack.append(token)
                        break
                    
                    if token.isalpha():
                        charBuffer.append(token)
                    elif token.isdigit():
                        finishReadChar = True
                        numBuffer.append(token)
                
                num = 0
                for strNum in numBuffer[::-1]:
                    num = num * 10 + int(strNum)
                stack += charBuffer[::-1] * num
                
        ans = ""
        for ele in stack:
            ans += ele
        return ans