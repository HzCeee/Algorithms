class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        rowsBuffer = [[] for _ in range(numRows)]
        rowIndex = 0
        step = 1
        for char in s:
            rowsBuffer[rowIndex].append(char)
            rowIndex += step
            if rowIndex == 0 or rowIndex == numRows - 1:
                step *= -1
        
        output = ""
        for row in rowsBuffer:
            output += "".join(row)
        
        return output
            