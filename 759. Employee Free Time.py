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
import heapq
class Solution:
    """
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals 
    """
    def employee_free_time(self, schedule: List[List[int]]) -> List[Interval]:
        # free time mean no interval and no overlap
        # if only one schedule return [] since not consider infinite
        res = []
        minheap = []

        #pre-handle schedule, push all intervals to minheap in sorted 
        for ls in schedule:
            for i in range(0, len(ls), 2):
                minheap.append([ls[i],ls[i+1]])
        heapq.heapify(minheap) # sort start

        # pop one first and comparing to rest
        flag = heapq.heappop(minheap)
        while minheap:
            first = heapq.heappop(minheap)
            # free time(nonoverlap)
            if flag[1] < first[0]:
                # update flag and add res
                res.append(Interval(start=flag[1], end=first[0]))
                flag = first
            else:
                # overlap then merge them which not free range
                flag[1] = max(flag[1], first[1])

        return res 

