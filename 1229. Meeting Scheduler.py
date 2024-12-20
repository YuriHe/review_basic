from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param slots1: The availability schedule of one.
    @param slots2: The availability schedule of one.
    @param duration: The expected duration of the meeting.
    @return: The earliest and appropriate meeting time in the interval for them.
    """
    def earliest_appropriate_duration(self, slots1: List[Interval], slots2: List[Interval], duration: int) -> Interval:
        # --- write your code here ---
        # find first overlapping and range >= duration
        # handle two array use two pointers, moving pointer which has less end value
        slots1.sort(key=lambda x: x.start)
        slots2.sort(key=lambda x: x.start)

        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            s1,s2 = slots1[i].start, slots2[j].start
            e1,e2 = slots1[i].end, slots2[j].end
            interactS = max(s1,s2)
            interfactE = min(e1,e2)
            if interfactE - interactS >= duration:
                return Interval(start=interactS, end=interactS+duration)
            # if not move smaller end to next timeslot 
            elif e1 < e2:
                i += 1
            else:
                j += 1
        return Interval(start=-1, end=-1)


