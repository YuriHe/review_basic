import heapq
class Solution:
    """
    Question: do loop for find two heaviest two stones and deduct them, until only one or no stone
    TOPIC: find 2 largest element -> maxheap(not default)
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            # at least 2 ele in heap
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, -abs(second-first))

        return 0 if len(heap) == 0 else -heap[0]