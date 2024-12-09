
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
        flag = intervals[0]
        for i in range(1, len(intervals)):
            if flag.end > intervals[i].start: # overlap
                return False
            # update flag
            flag = intervals[i]
        return True