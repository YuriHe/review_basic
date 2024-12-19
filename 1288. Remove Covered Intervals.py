class Solution:
    """
    Question:
    don delete ele in array 
    use earliest one as start point, largest index as end point which cover huge range
    handle [1,2] [1,4]
    """
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        ctn = 0

        intervals.sort(key=lambda x: (x[0], -x[1]))
        flag = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # check flag can totally cover cur interval, remove cur
            if flag[0] <= start and flag[1] >= end:
                # flag is [c, d]
                ctn += 1
            else:
                flag = intervals[i]


        return len(intervals) - ctn