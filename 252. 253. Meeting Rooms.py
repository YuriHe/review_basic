
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    Question: 252. Meeting Rooms
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0: return True

        # check if overlap
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start: # overlap
                return False
        return True

    # Question: 253. Meeting Rooms ii 
    # find minimum number of room required
    # 1solution: Sweep line algorithm
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Ask at most how many objects are overlapping at the same time
        # define points 2d array store[start/end point, +-1]
        points = []
        for interval in intervals:
            points.append([interval.start, 1])
            points.append([interval.end, -1])

        count, res = 0, 0
        for _, ctn in sorted(points):
            count += ctn
            res = max(res, count)
                return res
    # 2 solution minheap
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0

        intervals.sort(key=lambda x: x.start)
        minheap = []
        for interval in intervals:
            if minheap and interval.start >= minheap[0]:
                # can share same room so pop later push
                heapq.heappop(minheap)
            heapq.heappush(minheap, interval.end)
        return len(minheap)