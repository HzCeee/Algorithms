class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(str(format(n, "032b"))[::-1], 2)