import heapq
class Solution:
    """
    Question: do loop for find two heaviest two stones and deduct them, until only one or no stone
    TOPIC: find 2 largest element -> maxheap(not default)
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        while len(max_heap) > 1:
            heapq.heapify(max_heap)
            if len(max_heap) >= 2:
                l1 = heapq.heappop(max_heap)
                l2 = heapq.heappop(max_heap)
                heapq.heappush(max_heap, -abs(l1-l2))
        return -max_heap[0] if len(max_heap) == 1 else 0