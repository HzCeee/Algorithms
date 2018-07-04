class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numCount = {}
        for num in nums:
            if num not in numCount:
                numCount[num] = 0
            numCount[num] += 1
        
        import heapq
        heap = []
        for num, count in numCount.items():
            heapq.heappush(heap, (-count, num))
        
        ans = []
        for i in range(k):
            _, num = heapq.heappop(heap)
            ans.append(num)
            
        return ans