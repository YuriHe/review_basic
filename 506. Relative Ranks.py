"""
    Questions: Top 3 have Medal, others sort from 3+1, 3+2, 3+n
    Topic: compare largest -> maxheap(score, index)
    If need find largest.. use maxheap
"""
def findRelativeRanks(self, score: List[int]) -> List[str]:
    res = [None] * len(score)
    # create list store (score, index)
    pq = [(-num, index) for index, num in enumerate(score)]
    # max heapify, BUT NOT MEAN heap sorted!!
    heapq.heapify(pq)
    count = 0
    while len(pq) > 0: # each time heappop, will heapify again 
        num, rank = heapq.heappop(pq)
        if count == 0:
            res[rank]= "Gold Medal"
        elif count == 1:
            res[rank] = "Silver Medal"
        elif count == 2:
            res[rank] = "Bronze Medal"
        else:
            res[rank] = str(count+1)
        count += 1
    return res
    