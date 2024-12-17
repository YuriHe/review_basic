"""
    Question: maximum subsequence sum multiple minimum value from nums2 -> get maximum value
    zip num1 and num2, sort decreasing order based on nums2(max), how about subsequence -> keep iterate list and push/pop heap
    choose maxsum + maxnums2
"""
def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
    pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
    pairs = sorted(pairs, key=lambda x: -x[1])
    
    minheap = []
    n1sum  = 0
    res = 0
    for n1, n2 in pairs:
        n1sum += n1
        heapq.heappush(minheap, n1)
        if len(minheap) > k:
            top = heapq.heappop(minheap)
            n1sum -= top
        if len(minheap) == k: # not elif, must update res every iteration
            res = max(res, n1sum*n2)
        
    return res