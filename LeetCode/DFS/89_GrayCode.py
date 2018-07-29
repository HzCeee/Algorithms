class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # return (BOOL, LISTOFNUMBERS)
        def grayCodeHelper(num, curCount, visitedNums):
            if num in visitedNums:
                return (False, [])
            if curCount == 2**n:
                return (True, [num])
            
            visitedNums.add(num)
            binNum = format(num, "0" + str(n) + "b")
            for index, digit in enumerate(binNum):
                nextBinNum = binNum[:index] + str(1 - int(digit)) + binNum[index + 1:]
                nextNum = int(nextBinNum, 2)
                if nextNum not in visitedNums:
                    isValid, nums = grayCodeHelper(nextNum, curCount + 1, visitedNums)
                    if isValid:
                        return (isValid, [num] + nums)
            
            return (False, [])
        
        return grayCodeHelper(0, 1, set())[1]
        
        