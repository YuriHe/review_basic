# 56. Merge Intervals
class Solution:
    """
    Question:return non-overlapping intervals, merge overlapping
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        # sort intervals first 
        intervals.sort(key=lambda x: x[0])
        flag = intervals[0]
        for i in range(1, len(intervals)):
            cur_start = intervals[i][0]
            cur_end = intervals[i][-1]
            if flag[1] < cur_start: 
                # no overlap
                res.append(flag)
                # update flag
                flag = intervals[i]
            else:
                # overlap & update flag
                flag = [min(flag[0],cur_start),max(flag[1], cur_end)]
        # last one
        res.append(flag)
        return res
            

# 57. Insert Interval
class Solution:
    """
    Question: return non-overlapping sorted intervals, merge overlapping interval
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
    
        for i in range(len(intervals)):
            cur_start = intervals[i][0]  
            cur_end = intervals[i][1]          
            if newInterval[1] < cur_start:
                # insert new interval before intervals[i:]
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > cur_end:
                # insert interval[i] for now 
                res.append(intervals[i])
            else: 
                # overlap with newInterval
                # update newInterval instead of push into res
                newInterval = [min(cur_start, newInterval[0]), max(cur_end, newInterval[1])]
        res.append(newInterval)
        return res

        
"""
435. Non-overlapping Intervals
Question: count remove times for non-overlapping intervals in rest of list
[i1, j1],[i2, j2], j1 and i2 can same, non-overlapping
STEP:sort [0], if cur[0] < flag[1], count++, flag=min(flag[1], cur[1]), greedy get more possible nonoverlap
"""
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    if not intervals: return 0
    intervals = sorted(intervals, key=lambda x: x[0])
    res = 0
    flag = intervals[0]

    for i in range(1, len(intervals)):
        start, end = intervals[i][0], intervals[i][1]
        if start < flag[1]:
            # overlap
            res += 1
            flag[1] = min(flag[1], end) # make interval shorter
        else:
            # update flag
            flag = intervals[i]
    return res


"""
452. Minimum Number of Arrows to Burst Balloons
Question: return number of non-overlapping intervals
sort+interval
1. sort points based on end of enterval since focus on burst as many ballon
2.if cur > end, new interval ++
3. no need to consider merge because use points[i][0] > end decide increase arrow 
"""
#SOLUTION1: only think non-overlap
def findMinArrowShots(self, points: List[List[int]]) -> int:
    arrow = 1
    points.sort(key=lambda x: x[1]) # burst as many balloons as possible
    end = points[0][1]
    for i in range(1, len(points)):
        cur_start = points[i][0]
        cur_end = points[i][1]
        if end < cur_start:
            arrow += 1
            end = cur_end

    return arrow
# SOLUTION2: if think overlap scene eg.[[0,5],[3,7], [4,6]] shot three 
def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda x: x[1])
        res = 1 # at least one arrow
        flag = points[0]
        for i in range(1, len(points)):
            start, end = points[i][0], points[i][1]
            if start > flag[1]:
                # new shot
                res += 1
                flag = points[i]
            else:
                flag[1] = min(end, flag[1])
        return res