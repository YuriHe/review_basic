"""
    Question: merge not-sorted intervals compare [starti, endi] [startj, endj]
    Issue: do we need to update intervals after merge -> Fix by Sort first val
    T: O(nlogn) S: O(n) include res
    [1,6] [4,5]
"""
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 1: return intervals
    intervals.sort(key=lambda x: x[0])
    flag = intervals[0]
    res = [flag]
    for i in range(1, len(intervals)):
        start = intervals[i][0]
        end = intervals[i][1]
        if start <= flag[1]: # but won't < flag[0] since sorted
            # overflap
            flag[1] = max(flag[1], end)
        else:
            # new interval and update new flag
            res.append(intervals[i])
            flag = intervals[i]
    return res