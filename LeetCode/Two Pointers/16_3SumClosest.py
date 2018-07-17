class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        closestSum = float("inf")
        
        for i, num in enumerate(nums[0:-2]):
            l, r = i+1, length-1
            
            if num+nums[r]+nums[r-1] < target:
                if abs(closestSum - target) > abs(num+nums[r]+nums[r-1] - target):
                    closestSum = num+nums[r]+nums[r-1]
            elif num+nums[l]+nums[l+1] > target:
                if abs(closestSum - target) > abs(num+nums[l]+nums[l+1] - target):
                    closestSum = num+nums[l]+nums[l+1]
            else:
                while l < r:
                    if abs(closestSum - target) > abs(num+nums[l]+nums[r] - target):
                        closestSum = num+nums[l]+nums[r]
                    if num+nums[l]+nums[r] < target:
                        l += 1
                    elif num+nums[l]+nums[r] > target:
                        r -= 1
                    else:
                        return target
                    
        return closestSum
        