class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prevRow, curRow = [], []
        for row in range(1, rowIndex+2):
            for i in range(row):
                if i == 0 or i == row - 1:
                    curRow.append(1)
                else:
                    curRow.append(prevRow[i - 1] + prevRow[i])
            prevRow = curRow
            curRow = []
        return prevRow