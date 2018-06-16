class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def generateNextNumber(strNum):
            nextNumbers = []
            for i in range(len(strNum)):
                digit = int(strNum[i])
                if digit == 0:
                    nextDigits = [9, 1]
                elif digit == 9:
                    nextDigits = [8, 0]
                else:
                    nextDigits = [digit - 1, digit + 1]
                for nextDigit in nextDigits:
                    nextNumbers.append(
                        strNum[:i] + str(nextDigit) + strNum[i+1:]
                    )
            return nextNumbers
        
        numQueue = [("0000", 0)]
        triedNum = []
        while numQueue:
            curNum, moveCount = numQueue.pop(0)
            triedNum.append(curNum)
            
            if curNum == target:
                return moveCount
            elif curNum in deadends:
                continue
            else:
                for nextNum in generateNextNumber(curNum):
                    if nextNum not in triedNum: 
                        numQueue.append((nextNum, moveCount + 1))
        
        return -1
                    
                