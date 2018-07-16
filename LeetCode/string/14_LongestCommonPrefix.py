class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not any(strs): return ""
        
        prefix = ""
        strs = sorted(strs, key=lambda x: len(x))
        charIndex = 0
        if charIndex >= len(strs[0]): return ""
        while True:
            curChar = strs[0][charIndex]
            for string in strs[1:]:
                if string[charIndex] != curChar:
                    return prefix
            prefix += curChar
            charIndex += 1
            if charIndex == len(strs[0]):
                return strs[0]
            
        return prefix
            