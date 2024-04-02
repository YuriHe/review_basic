import heapq
class Solution:
    """
    Question: find k closet points in 2d array to (0,0), if same distance, return all
    -> find k smallest distance MAXHEAP(NOT DEFAULT)
    T: nlogk
    S: k
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for a, b in points:
            dis = a**2 + b**2
            heapq.heappush(heap, (-dis, [a,b]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [points for dis, points in heap]




