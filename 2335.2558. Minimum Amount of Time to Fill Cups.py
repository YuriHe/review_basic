from typing import List
import heapq

# 2335. Minimum Amount of Time to Fill Cups,
'''
    QUESTION: every second can choose 2 diff cups or 1 cup,
    [cold, warm, hot], return minimum seconds for fill all these 3 cups
    [-4,-2,-1]->[-3,-1,-1]->[-2,-1,0]->...
    [-5,0,0] ->[-4,0,1]...
'''
def fillCups(amount: List[int]) -> int:
    max_heap = [-v for v in amount] 
    heapq.heapify(max_heap)
    res = 0
    while max_heap[0] < 0: # peek/top
        max1 = -heapq.heappop(max_heap)  # pop first largest #4
        max2 = -heapq.heappop(max_heap) # pop second largest #2
        heapq.heappush(max_heap, -(max1-1))
        heapq.heappush(max_heap, -(max2-1))
        res += 1
    return res


print(fillCups([0,0,5]))


#############################
# 2558. Take Gifts From the Richest Piles
'''
    QUESTION:provided list of pile. each pile is with num of gifts. 
    Every second will pick pile with maximum num of gifts and must leave square root of gifts. if < square root of gifts then keep it. 
    Use Max-heap, keep sort and update v
    TIME: nlogn SPACE: n
'''
def pickGifts(self, gifts: List[int], k: int) -> int:
    max_heap = [-v for v in gifts]
    heapq.heapify(max_heap)
    while -max_heap[0] > math.floor(math.sqrt(-max_heap[0])) and k > 0:
        max1 = -heapq.heappop(max_heap)
        left = math.floor(math.sqrt(max1))
        heapq.heappush(max_heap, -left)
        k -=1

    return -sum(max_heap)