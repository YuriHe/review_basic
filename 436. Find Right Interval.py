class Solution:
    """
    Question:
    read Q; find minimum start as right interval for i 
    start of each interval is unique
    sort + binary search starting point
    O(nlogn)
    """
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = [-1] * len(intervals)
        # create dic to map interval start points to their indices
        startMap = {interval[0]: i for i, interval in enumerate(intervals)}
        # extract list of start points and sort them for binary search
        startLs = sorted(startMap.keys())

        for i, interval in enumerate(intervals):
            # find smallest start point >= interval.end
            pos = self.bs(startLs, interval[1])
            if pos != -1:
                res[i] = startMap[startLs[pos]]

        return res

    def bs(self, array, v):
        lo, hi = 0, len(array) - 1
        first = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if array[mid] >= v:# find that, find smaller one
                hi = mid - 1
                first = mid
            else:
                lo = mid + 1
        return first
                
