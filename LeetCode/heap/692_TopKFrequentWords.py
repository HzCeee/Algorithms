class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        wordCount = {}
        for word in words:
            if word not in wordCount:
                wordCount[word] = 0
            wordCount[word] += 1
        
        import heapq
        heap = []
        for word, count in wordCount.items():
            heapq.heappush(heap, (-count, word))
        
        ans = []
        for i in range(k):
            _, word = heapq.heappop(heap)
            ans.append(word)
        
        return ans