"""
    Question: find Kth largest element from list
    Topic: Minheap(PQ)!(NOT MAX HEAP) use size k, smallest of k largest eles on top
"""
def findKthLargest(self, nums: List[int], k: int) -> int:
    # create heap list 
    heap = []
    # build heap with k size and heapify O(nlogn)
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
    