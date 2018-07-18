class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from functools import reduce
        candidates = list(range(1, n + 1))
        output = ""
        for digit in range(n - 1):
            permutationNum = reduce(lambda x, y: x * y, range(1, n - digit)) if digit < n - 2 else 1
            numIndex = (k-1) // permutationNum
            k -= numIndex * permutationNum
            output += str(candidates.pop(numIndex))
        
        return output + str(candidates[0])
            