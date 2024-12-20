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
            s1,s2 = firstList[i][0], secondList[j][0]
            e1,e2 = firstList[i][1], secondList[j][1]
            # interfact
            interS = max(s1,s2)
            interE = min(e1, e2)
            duration = interE - interS 
            if duration >= 0:
                # mean overlap/intersect
                res.append([interS, interS+duration])

            if e1 < e2: # move smaller end for more space to add overlapping interval
                i += 1
            else:
                j += 1
        return res