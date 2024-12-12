from typing import List
import heapq

# 2335. Minimum Amount of Time to Fill Cups,
"""
    Question:minimum fillup cups with two options: 2cup and 1cup
    [cold, warm, hot], return minimum seconds for fill all these 3 cups
    [-4,-2,-1]->[-3,-1,-1]->[-2,-1,0]->...
    [-5,0,0] ->[-4,0,1]...
    Topic: Choose max amount water first and also second max amount water until decrement to 0
    Heap opeation:
    default is min heap, max heap convert to negate
    create heap_ls 
    heapq.heapify(heap_ls)
    heapq.heappop(heap_ls)
    heapq.heappush(heap_ls, v)
"""
def fillCups(self, amount: List[int]) -> int:
    res = 0
    # 1.create max heap negate list based on amount list 0(n)
    max_heap_ls = [-n for n in amount]
    # 2.heapify in original ls, O(n)
    heapq.heapify(max_heap_ls)
    # 3.iterate amount ls, update each water after second(pop-> push)
    while max_heap_ls[0] < 0: 
        # at most two water
        first = -heapq.heappop(max_heap_ls)-1 # negate->postive
        second = -heapq.heappop(max_heap_ls)-1 
        heapq.heappush(max_heap_ls, -first)
        heapq.heappush(max_heap_ls, -second)
        res += 1
    return res



#############################
# 2558. Take Gifts From the Richest Piles
'''
    QUESTION:provided list of pile. each pile is with num of gifts. 
    Every second will pick pile with maximum num of gifts and must leave square root of gifts. if < square root of gifts then keep it. 
    Use Max-heap, keep sort and update v
    TIME: nlogn SPACE: n
'''
def pickGifts(self, gifts: List[int], k: int) -> int:
    # SOLUTION1: brute force
    while k > 0:
            curMax = max(gifts)
            gifts.remove(curMax) # remove first one
            # choose max
            newV = math.floor(math.sqrt(curMax))
            gifts.append(newV)
            k-=1
        return sum(gifts)
    
    # SOLUTION2: heap
    max_heap = [-v for v in gifts]
    heapq.heapify(max_heap)
    while k > 0:
        max1 = -heapq.heappop(max_heap)
        left = math.floor(math.sqrt(max1))
        heapq.heappush(max_heap, -left)
        k -=1

    return -sum(max_heap)