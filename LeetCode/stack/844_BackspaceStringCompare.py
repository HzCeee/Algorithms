class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        typedS = []
        for char in S:
            if char == "#" and typedS:
                typedS.pop()
            elif char.isalpha():
                typedS.append(char)
        
        typedT = []
        for char in T:
            if char == "#" and typedT:
                typedT.pop()
            elif char.isalpha():
                typedT.append(char)
                
        return typedS == typedT