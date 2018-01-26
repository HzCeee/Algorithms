def numSubarrayProductLessThanK(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # leftPtr denotes the index of the leftmost element in the checked subarray
    # rightPtr denotes the index of the rightmost element in the checked subarray
    
    count = 0
    
    for rightPtr in range(len(nums)):
        leftPtr = rightPtr
        product = 1
        while leftPtr >= 0:
            product = product * nums[leftPtr]
            if product < k: 
                count += 1
            else:
                break
                
            leftPtr -= 1
    
    return count

def numSubarrayProductLessThanK(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # leftPtr denotes the index of the leftmost element in the checked subarray
    # rightPtr denotes the index of the rightmost element in the checked subarray
    
    count = 0
    oldRightPtr = -1
    
    for leftPtr in range(len(nums)):
        product = 1
        
        rightPtr = leftPtr
        while rightPtr < len(nums):
            product *= nums[rightPtr]
            if product >= k: break
            rightPtr += 1
        rightPtr -= 1
        
        if oldRightPtr == rightPtr: continue
        
        lengthIncrease = 0 if rightPtr < leftPtr else rightPtr - leftPtr + 1
        lengthDecrease = 0 if oldRightPtr < leftPtr else oldRightPtr - leftPtr + 1
        
        count = count + (1 + lengthIncrease) * lengthIncrease / 2 - (1 + lengthDecrease) * lengthDecrease / 2
        
        if rightPtr >= len(nums) - 1: break
            
        oldRightPtr = rightPtr
    
    return int(count)