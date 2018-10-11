# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

        endpoints = []
        for interval in intervals:
            endpoints.append(Endpoint(time=interval.start, is_start=True))
            endpoints.append(Endpoint(time=interval.end, is_start=False))
        
        endpoints.sort()
        
        used_rooms, max_rooms = 0, 0
        for meeting_time in endpoints:
            if meeting_time.is_start:
                used_rooms += 1
                max_rooms = max(used_rooms, max_rooms)
            else:
                used_rooms -= 1
        return max_rooms
        