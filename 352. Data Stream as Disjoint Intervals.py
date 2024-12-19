"""
Question: Data stream is running list of contiguous number
1way: use set to store pushed ele and sort; when search interval, we only need to check if gap
[1,2,3,6,7]
2way: treemap or say SortedDict in python3
"""
from sortedcontainers import SortedDict

class SummaryRanges:
    # SOLUTION1: nlogn
    def __init__(self):
        self.numSet = set()
        
    def addNum(self, value: int) -> None:
        self.numSet.add(value)

    def getIntervals(self) -> List[List[int]]:
        res = []
        ls = sorted(self.numSet)
        i = 0 # right pointer
        while i < len(ls):
            start = ls[i]
            while i+1 < len(ls) and ls[i] + 1 == ls[i+1]:
                i += 1
            res.append([start, ls[i]])
            i+= 1
        return res

    # 2SOLUTION use sortdict sort key which is number
"""
insertion, deletion O(logn)
access by key O(logn)
iteration O(n)
"""
from sortedcontainers import SortedDict
def __init__(self):
    self.treeMap = SortedDict()
def addNum(self, value: int) -> None:
    self.treeMap[value] = True
def getIntervals(self) -> List[List[int]]:
    res = []
    for n in self.treeMap:
        if res and res[-1][1] + 1 == n:
            # update last res
            res[-1][1] = n
        else:
            res.append([n, n])
    return res





        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()