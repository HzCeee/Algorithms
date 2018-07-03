class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # return true or false whether all houses have been covered
        # TLE
#         def findRadiusHelper(midRadius):
#             for house in houses:
#                 if not any(map(lambda heaterPos: heaterPos - midRadius <= house <= heaterPos + midRadius, heaters)):
#                     return False
#             return True
        
#         lowRadius, highRadius = 0, max(max(houses) - min(heaters), max(heaters) - min(houses))
#         while lowRadius <= highRadius:
#             midRadius = (lowRadius + highRadius) // 2
#             covered = findRadiusHelper(midRadius)
#             biggerCovered = findRadiusHelper(midRadius + 1)
#             if not covered and biggerCovered:
#                 return midRadius + 1
#             elif covered and biggerCovered:
#                 highRadius = midRadius - 1
#             else:
#                 lowRadius = midRadius + 1
            
#         return 0

        def findRadiusHelper(nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        heaters.sort()
        result = float("-inf")

        for house in houses :
            index = findRadiusHelper(heaters, house)
            leftHeaterDistance = house - heaters[index - 1] if index > 0 else float("inf")
            rightHeaterDistance = heaters[index] - house if index < len(heaters) else float("inf")
            
            result = max(result , min(leftHeaterDistance, rightHeaterDistance))

        return result