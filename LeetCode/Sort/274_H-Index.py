class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        citationCount = [0]*(n+1)
        for c in citations:
            citationCount[min(n, c)] += 1
        summ = 0
        for i in range(n, -1, -1):
            summ += citationCount[i]
            if summ >= i:
                return i