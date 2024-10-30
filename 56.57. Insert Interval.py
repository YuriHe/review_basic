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
                flag = intervals[i]
            else:
                # overlap
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

        