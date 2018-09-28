class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum(map(lambda x: int(x)**2, str(n)))
        return True