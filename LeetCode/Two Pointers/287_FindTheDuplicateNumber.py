class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        "array nums containing n + 1 integers where each integer is between 1 and n (inclusive)" 
        makes the array an abstracted linked list: nums[num] -> newNum. 
        Now since integer cannot be 0, item 0 is guarenteed to be a "node" outside any cycle because nums[num] must be larger than 0. 
        Then the 1st fast-slow traverse is guranteed to have the meet point at equally distance from the common starting point (0) to the cycle entry point
        '''
        fastPtr = 0
        slowPtr = 0
        
        while (fastPtr == 0 and slowPtr == 0) or fastPtr != slowPtr:
            fastPtr, slowPtr = nums[nums[fastPtr]], nums[slowPtr]
            
        circleEntryPtr = 0 # the circle entry is a position of the duplicated numbers
        
        while circleEntryPtr != slowPtr:
            circleEntryPtr, slowPtr = nums[circleEntryPtr], nums[slowPtr]
            
        return circleEntryPtr