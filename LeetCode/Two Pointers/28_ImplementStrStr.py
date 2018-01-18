class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle:
            return 0
        
        needleLength = len(needle)
        for index in range(len(haystack)):
            if haystack[index: index+needleLength] == needle:
                return index
        
        return -1