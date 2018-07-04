class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        charCount = {}
        for char in s:
            if char not in charCount: 
                charCount[char] = 0
            charCount[char] += 1
        
        import heapq
        heap = []
        for char, count in charCount.items():
            heapq.heappush(heap, (-count, char))
        
        ans = ""
        while heap:
            count, char = heapq.heappop(heap)
            ans += (-count)*char
        
        return ans