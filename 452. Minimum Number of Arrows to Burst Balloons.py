class Solution:
    """
    Question: return number of non-overlapping intervals
    sort+interval
    1. sort points based on end of enterval since focus on burst as many ballon
    2.if cur > end, new interval ++
    3. no need to consider merge because use points[i][0] > end decide increase arrow 
    """
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