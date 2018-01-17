class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            
            if nums[low] < nums[mid]:
                if nums[low] <= target < nums[mid]: # normal binary search
                    high = mid - 1
                else: # narrow search range in Rotated Sorted Array
                    low = mid + 1
            elif nums[low] == nums[mid]: # in this case, low = mid = high or high = low + 1
                low = mid + 1
            else:
                if nums[mid] < target <= nums[high]: # normal binary search
                    low = mid + 1
                else: # narrow search range in Rotated Sorted Array
                    high = mid - 1
        
        return -1