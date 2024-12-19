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
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    """
    Question: 
    Sweep line, one need to care start,end
    after sort -1<1
    """
    def count_of_airplanes(self, airplanes: List[Interval]) -> int:
        # Sweep Line 
        if not airplanes: return 0
        
        # create nested [startp,endp]
        points = []
        for plane in airplanes:
            # take off
            points.append([plane.start, 1])
            # land
            points.append([plane.end, -1])

        count, res = 0, 0
        for _, ctn in sorted(points):
            count += ctn
            res = max(res, count)
        return res

