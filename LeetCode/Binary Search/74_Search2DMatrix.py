class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        firstNumbers = [nums[0] for nums in matrix]
        
        # find row
        low, high = 0, len(firstNumbers) - 1
        while low <= high:
            mid = (low + high) // 2
            if firstNumbers[mid] == target:
                return True
            elif firstNumbers[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        # find element in previous found row
        searchNumbers = matrix[high]
        low, high = 0, len(searchNumbers) - 1
        while low <= high:
            mid = (low + high) // 2
            if searchNumbers[mid] == target:
                return True
            elif searchNumbers[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False