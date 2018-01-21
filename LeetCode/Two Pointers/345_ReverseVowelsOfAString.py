class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # left denotes the index of left vowels
        # right denotes the index of right vowels
        
        vowel = 'AEIOUaeiou'
        s = list(s)
        left, right = 0, len(s)-1
        while left < right:
            while s[left] not in vowel and left < right:
                left = left + 1
            while s[right] not in vowel and left < right:
                right = right - 1
                
            s[left], s[right] = s[right], s[left]
            
            left, right = left + 1, right - 1
        return ''.join(s)