class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if len(heap) == k: 
                    heapq.heappush(heap, -matrix[row][col])
                    heapq.heappop(heap)
                else: 
                    heapq.heappush(heap,-matrix[row][col])
        return -heapq.heappop(heap)
                