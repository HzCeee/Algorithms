class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # return True if num is an additive sequence given num1Len and num2Len
        def isAdditiveNumberHelper(num1Len, num2Len, strNum):
            num1, num2 = int(strNum[:num1Len]), int(strNum[num1Len: num1Len+num2Len])
            if len(str(num1)) != num1Len or len(str(num2)) != num2Len:
                return False
            
            nextNum = num1 + num2
            nextNumLen = len(str(nextNum))
            
            if nextNumLen + num1Len + num2Len == len(strNum):
                return True if int(strNum[-nextNumLen:]) == nextNum else False
            elif nextNumLen + num1Len + num2Len > len(strNum):
                return False
            else:
                expectedNum = int(strNum[num1Len+num2Len: num1Len+num2Len+nextNumLen])
                if len(str(expectedNum)) != nextNumLen or expectedNum != nextNum:
                    return False
                return isAdditiveNumberHelper(num2Len, nextNumLen, strNum[num1Len:])
        
        for num1Len in range(1, (len(num) - 1) // 2 + 1):
            for num2Len in range(1, (len(num) - num1Len) // 2 + 1):
                if isAdditiveNumberHelper(num1Len, num2Len, num):
                    return True
        return False
            
                