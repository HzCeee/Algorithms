class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counts = collections.Counter(S)
        _, times = counts.most_common(1)[0]
        if times > math.ceil(len(S) / 2):
            return ""
        heap = []
        for letter, times in counts.items():
            heap.append([-times, letter, times])
        heapq.heapify(heap)
        ans = ''
        while heap:
            _, letter, times = heapq.heappop(heap)
            if not ans or letter != ans[-1]:
                ans += letter
                times -= 1
                if times > 0:
                    heapq.heappush(heap, [-times, letter, times])
            else:
                _, letter2, times2 = heapq.heappop(heap)
                ans += letter2
                times2 -= 1
                if times2 > 0:
                    heapq.heappush(heap, [-times2, letter2, times2])
                heapq.heappush(heap, [-times, letter, times])
        return ans