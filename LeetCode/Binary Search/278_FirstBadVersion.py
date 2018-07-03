# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lowVer, highVer = 1, n
        while lowVer <= highVer:
            midVer = (lowVer + highVer) // 2
            isBad = isBadVersion(midVer)
            isNextBad = isBadVersion(midVer + 1)
            if not isBad and isNextBad:
                return midVer + 1
            elif isBad and isNextBad:
                highVer = midVer - 1
            else:
                lowVer = midVer + 1
                
        return 1
            