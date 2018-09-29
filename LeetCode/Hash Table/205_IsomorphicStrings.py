class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        STMapping, TSMapping = dict(), dict()
        for index, char in enumerate(s):
            if char not in STMapping:
                STMapping[char] = t[index]
            if t[index] not in TSMapping:
                TSMapping[t[index]] = char
            
            if STMapping[char] != t[index] or TSMapping[t[index]] != char:
                return False
        
        return True