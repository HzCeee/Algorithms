class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for idx in range(len(num)):
            while stack and k > 0:
                if num[idx] >= stack[-1]: break
                stack.pop()
                k -= 1
            stack.append(num[idx])
             
        while k != 0:
            stack.pop()
            k -= 1
        
        while stack and stack[0] == '0':
            stack = stack[1:]
        
        return ''.join(stack) or '0'
    