"""
    Question:Find two largest elements
    Topic:Max heap, sort -> find two largest
    Solution1: heap T:O(n) S:O(n)
    Solution2: compare T:O(n) S:O(1)
"""
import heapq

def maxProduct(self, nums: List[int]) -> int:
    # # Solution1: Maxheap(default is minheap)
    # 1.create negate list O(n)
    ls = [-n for n in nums]
    # 2.heapify O(n)
    heapq.heapify(ls)
    # 3.heappop operation O(logn)
    first_l = heapq.heappop(ls)
    second_l = heapq.heappop(ls)
    return (abs(first_l)-1) * (abs(second_l)-1)

    # Solution2: compare
    # 1.declare first second to -1 since all >= 1
    # 2.compare second first then larger first
    first_l, second_l = -1, -1
    for n in nums:
        if n > second_l:
            second_l = n
        if second_l > first_l:
            # switch
            temp = first_l
            first_l = second_l
            second_l = temp
    return (first_l-1) * (second_l-1)