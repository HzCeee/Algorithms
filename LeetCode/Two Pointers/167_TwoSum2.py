class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # index1 denotes the index of the first number
        # index2 denotes the index of the second number
        
        index1, index2 = 0, len(numbers) - 1
        while index1 < index2:
            if numbers[index1] + numbers[index2] != target:
                if numbers[index1] + numbers[index2] < target:
                    index1 += 1
                else:
                    index2 -= 1
            else:
                return [index1 + 1, index2 + 1]