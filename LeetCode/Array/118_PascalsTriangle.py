class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        for row in range(1, numRows + 1):
            nums = []
            for i in range(row):
                if i == 0 or i == row - 1:
                    nums.append(1)
                else:
                    nums.append(output[row - 2][i - 1] + output[row - 2][i])
            output.append(nums)
        return output