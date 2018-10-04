class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        r, b, g = 0,0,0
        for rc, bc, gc in costs:
            r, b, g = rc+min(b, g), bc+min(r, g), gc+min(r, b)
        return min([r, b, g])
        