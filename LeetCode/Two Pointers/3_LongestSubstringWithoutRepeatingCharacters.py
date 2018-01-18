class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # consider substring s[left: right]

        left = right = 0
        maxLength = 0
        while right < len(s):
            if s[right] not in s[left: right]:
                right += 1
            else:
                while s[left] != s[right]:
                    left += 1
                left += 1
            maxLength = max(maxLength, right - left)
        return maxLength