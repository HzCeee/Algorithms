class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # left denotes the index of left compared charactor
        # right denotes the index of right compared charactor
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if (s[left].isalpha() or s[left].isdigit()) and (s[right].isalpha() or s[right].isdigit()):
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
            else:
                if not s[left].isalpha() and not s[left].isdigit():
                    left += 1
                if not s[right].isalpha() and not s[right].isdigit():
                    right -= 1
        
        return True