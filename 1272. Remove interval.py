from typing import (
    List,
)

class Solution:
    """
    @param intervals: A sorted list of disjoint intervals.
    @param to_be_removed: An interval to be removed.
    @return: A set of real numbers.
    """
    def delete_interval(self, intervals: List[List[int]], to_be_removed: List[int]) -> List[List[int]]:
        """
        intervals is sorted disjoin; to_be_removed is interval 
        return list intervals that deleted range 
        add right overlap,
        add left overlap, 
        to_be_removed inside of current interval which will add head and tail
        """
        res = []
        for i in range(len(intervals)):
            cur = intervals[i]
            # non-overlap [a,b)
            if cur[1] <= to_be_removed[0] or cur[0] >= to_be_removed[1]:
                res.append(cur)
            else:
                # left overlap
                if cur[0] < to_be_removed[0]:
                    new_interval = [cur[0], to_be_removed[0]]
                    res.append(new_interval)
                # left overlap 
                if cur[1] > to_be_removed[1]:
                    new_interval = [to_be_removed[1], cur[1]]
                    res.append(new_interval)
        return res


