class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) > 1:
            tmpSum = 0
            for digit in str(num):
                tmpSum += int(digit)
            num = tmpSum
        return num