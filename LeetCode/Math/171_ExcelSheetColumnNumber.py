class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        for index, char in enumerate(s):
            weight = 26 ** (len(s) - index - 1)
            number += weight * (ord(char) - ord("A") + 1)
        return number