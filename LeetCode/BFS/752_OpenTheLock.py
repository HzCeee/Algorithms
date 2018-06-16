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
                    nextDigits = [1, 9]
                elif digit == 9:
                    nextDigits = [0, 8]
                else:
                    nextDigits = [digit + 1, digit - 1]
                for nextDigit in nextDigits:
                    nextNumbers.append(
                        strNum[:i] + str(nextDigit) + strNum[i+1:]
                    )
            return nextNumbers
        
        numCountQueue = [("0000", 0)]
        numQueue = set(["0000"])
        triedNum = []
        while numQueue:
            curNum, moveCount = numCountQueue.pop(0)
            triedNum.append(curNum)
            # print(triedNum)
            
            if curNum == target:
                return moveCount
            elif curNum in deadends:
                continue
            else:
                for nextNum in generateNextNumber(curNum):
                    if nextNum not in triedNum and nextNum not in numQueue: 
                        numCountQueue.append((nextNum, moveCount + 1))
                        numQueue.add(nextNum)
        
        return -1