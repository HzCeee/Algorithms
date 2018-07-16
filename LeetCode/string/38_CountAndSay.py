class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        curSay = "1"
        for count in range(1, n):
            initPtr, curPtr = 0, 0
            nextSay = ""
            for curPtr in range(len(curSay)):
                if curSay[curPtr] != curSay[initPtr]:
                    nextSay += str(curPtr - initPtr)
                    nextSay += curSay[initPtr]
                    initPtr = curPtr
            nextSay += str(curPtr - initPtr + 1)
            nextSay += curSay[initPtr]
            curSay = nextSay
        
        return curSay
                    