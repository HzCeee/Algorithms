class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        charCount = dict()
        for char in s:
            if char not in charCount:
                charCount[char] = 0
            charCount[char] += 1
        for char in t:
            if char not in charCount:
                return False
            charCount[char] -= 1
            if charCount[char] < 0:
                return False
        for value in charCount.values():
            if value != 0:
                return False
        return True
        