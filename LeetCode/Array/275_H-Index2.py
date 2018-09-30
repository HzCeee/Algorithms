class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        for hIndex in range(1, min(len(citations)+1, citations[-1]+1))[::-1]:
            i = len(citations) - hIndex
            if citations[i] >= hIndex:
                return hIndex
        return 0
            