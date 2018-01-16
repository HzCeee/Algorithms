class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, num in enumerate(numbers):
            targetNum = target - num
            
            low, high = 0, len(numbers) - 1
            
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == targetNum and mid != index:
                    index1 = min(index, mid) + 1
                    index2 = max(index, mid) + 1
                    return [index1, index2]
                elif numbers[mid] <= targetNum:
                    low = mid + 1
                elif numbers[mid] > targetNum:
                    high = mid - 1