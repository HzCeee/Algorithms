class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # sPtr denotes the pointer in string s
        # tPtr denotes the pointer in stirng t
        if not s:
            return True
        
        sPtr = 0
        for tPtr in range(len(t)):
            if t[tPtr] == s[sPtr]:
                sPtr += 1
                if sPtr == len(s): return True
        
        return False