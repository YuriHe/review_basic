class Solution:
    """
    Question: overlap interval
    already sorted
    1.use two pointers to track both list. since need to find overlap between them, so only consider while and . DONT consider extra ele in list
    2.check which end smaller, then ++
    """
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            # define boundaries
            s1,s2,e1,e2 = firstList[i][0], secondList[j][0], firstList[i][1], secondList[j][1]
            # defind overlap parts
            l, r = max(s1,s2), min(e1, e2)
            if l <= r:
                res.append([l,r])
            
            # move pointer
            if e1 < e2:
                i += 1
            else:
                j+= 1
        return res