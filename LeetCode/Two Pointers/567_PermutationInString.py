class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # leftPtr denotes the left index of the checked string
        # rightPtr denotes the index after the rightmost element of the checked string
        
        target = dict()
        for char in s1:
            target[char] = 1 if char not in target else target[char] + 1
        
        check = dict()
        for char in s2[: len(s1) - 1]:
            check[char] = 1 if char not in check else check[char] + 1
            
        leftPtr = 0
        
        for rightPtr in range(len(s1), len(s2) + 1):
            check[s2[rightPtr - 1]] = 1 if s2[rightPtr - 1] not in check else check[s2[rightPtr - 1]] + 1
            
            if check == target: return True
            
            check[s2[leftPtr]] -= 1
            if check[s2[leftPtr]] == 0: check.pop(s2[leftPtr])
                
            leftPtr += 1
            
        return False