class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: 
            return []
        
        prevNum, possibleEndNum = nums[0], None
        rangeList = [str(prevNum)]
        for i, num in enumerate(nums[1:]):
            if num == prevNum + 1:
                if i == len(nums) - 2: 
                    rangeList[-1] += "->{}".format(num)
                possibleEndNum, prevNum = num, num
            else:
                if possibleEndNum:
                    rangeList[-1] += "->{}".format(possibleEndNum)
                    possibleEndNum = None
                prevNum = num
                rangeList.append(str(num))
        return rangeList
                
        