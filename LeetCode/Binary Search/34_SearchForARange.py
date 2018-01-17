class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        low, high = 0, len(nums) - 1
        found = False
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] <= target: # find the ending position of target value
                if nums[mid] == target:
                    found = True
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1 
                
        if not found: return [-1, -1]
        highIndex = low
        
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] >= target: # find the starting position of target value
                high = mid - 1
                
        lowIndex = high
        
        return [lowIndex + 1, highIndex - 1]