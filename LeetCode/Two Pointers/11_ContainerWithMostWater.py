class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # left, right denotes the indexes of 2 borders

        left, right = 0, len(height) - 1
        maxVolume = 0
        
        while left < right:
            minHeight = min(height[left], height[right])
            maxVolume = max(maxVolume, (right - left) * minHeight)
            if height[left] < height[right]:
                while left <= len(height) - 1 and height[left] <= minHeight:
                    left += 1
            else:
                while right >= 0 and height[right] <= minHeight:
                    right -= 1
                    
        return maxVolume