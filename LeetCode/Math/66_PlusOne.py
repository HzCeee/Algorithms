class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            return digits[:-1] + [digits[-1] + 1]
        
        carry = 1
        for i, digit in enumerate(digits[::-1]):
            oriIndex = len(digits) - 1 - i
            if digit + carry == 10:
                digits[oriIndex] = 0
                carry = 1
            else:
                digits[oriIndex] = digit + 1
                return digits
            
        if carry == 1:
            return [1] + digits
                