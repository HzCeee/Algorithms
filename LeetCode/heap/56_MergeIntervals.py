# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import heappush, heappop

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        
        heap = []
        for interval in intervals:
            heappush(heap, [interval.start, interval.end])
        
        result = []
        while len(heap) >= 2:
            leftInterval, rightInterval = heappop(heap), heappop(heap)
            if rightInterval[0] <= leftInterval[1]:
                newInterval = [leftInterval[0], max(rightInterval[1], leftInterval[1])]
                heappush(heap, newInterval)
            else:
                heappush(heap, rightInterval)
                result.append(leftInterval)
        
        if heap: result.append(heap[0])
            
        return result
        
        