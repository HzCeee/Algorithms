class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
        self.length = 0
        self.minVal = {0: float("inf")}
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.minVal[self.length + 1] = min(self.minVal[self.length], x)
        self.length += 1
        
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        self.minVal.pop(self.length)
        self.length -= 1
        
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minVal[self.length]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()