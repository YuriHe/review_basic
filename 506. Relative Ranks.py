"""
    Questions: Top 3 have Medal, others sort from 3+1, 3+2, 3+n
    Topic: compare largest -> maxheap(score, index)
    If need find largest.. use maxheap
"""
def findRelativeRanks(self, score: List[int]) -> List[str]:
    res = [0] * len(score)
    heap = [(-v, i) for i, v in enumerate(score)]
    heapq.heapify(heap)
    
    rank = 0
    while heap:
        num, idx = heapq.heappop(heap)
        if rank == 0:
            res[idx]= "Gold Medal"
        elif rank == 1:
            res[idx] = "Silver Medal"
        elif rank == 2:
            res[idx] = "Bronze Medal"
        else:
            res[idx] = str(rank+1)
        rank += 1

    return res
    