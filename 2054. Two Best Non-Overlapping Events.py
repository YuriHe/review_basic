class Solution:
    """
    Question: noon-overlapping interval
    1.choose no overlap intervals, at most two, one or two (use replace to control number: maxVal)
    2.find maxium value
    -> minheap sort
    """
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # create heap store (endtime, val)
        heap = []
        maxVal = 0 # use for find best nonoverlap val from previous intervals which store in heap
        maxSum = 0

        events.sort(key=lambda x: x[0])
        
        # go through all events
        for event in events:
            # if first ele in q < event.star, update maxVal and removel all eles in heap before current event starts
            while heap and heap[0][0] < event[0]:
                maxVal = max(maxVal, heap[0][1])
                heapq.heappop(heap)
            
            # update sum max
            maxSum = max(maxSum, maxVal+event[2])
            # push
            heapq.heappush(heap, (event[1], event[2]))
        return maxSum
