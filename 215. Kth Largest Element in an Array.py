# """
#     Question: find Kth largest element from list
#     Topic: Minheap(PQ)!(NOT MAX HEAP) use size k, smallest of k largest eles on top
# """
def findKthLargest(self, nums: List[int], k: int) -> int:
    """
        SOLUTION1: Use Max heap(not default, invert value to simulate max-heap)
        insert all elements and pop largest element k times to get result
    """
    # create list 
    heap = [-num for num in nums]
    # heapify the list, O(nlogn)
    heapq.heapify(heap) 
    # pop largest element k times to get result
    while k > 0:
        res = heapq.heappop(heap)
        k-= 1
    return -res

    """
        SOLUTION2: Use Minheap, 
        keep size of heap limited to k elements. 
        insert and handle size as well
        pop smaller(pop root of heap)
        root of heap always contains Kth largest element
        return heap[0] which kth largest
    """
    # store all nums to heap list and heapify
    # pop the heap k times
    # T: O(nlogn)
    heap = [n for n in nums] # or nums.copy()
    heapq.heapify(heap)
    while len(heap) > k:
        heapq.heappop(heap)

    return heap[0]

    # or keep k size O(nlogk)
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            # pop
            heapq.heappop(heap)
    return heap[0]


# SOLUTION3: Quicksort-quickselect only recur kth largest
# O(n), but worst O(n^2)
# TLE
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            # randomely select pivot index before[left,right]
            pivot_index = random.randint(left,right)
            # After partition, smaller | new pivot index | larger
            new_pivot = self.partition(nums, left, right, pivot_index)
            # check pivot pos if desired k-th largest index
            if new_pivot == len(nums)-k:
                return nums[new_pivot]
            elif new_pivot < len(nums)-k:
                left = new_pivot + 1
            else:
                right = new_pivot - 1
    
    # This is template for quicksort
    def partition(self, nums, left, right, pivot_index):
        # find pivot at cur pivot index
        pivot = nums[pivot_index]
        # move pivot to last element 
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index] 
        # set low 
        low = left 
        for i in range(left, right): # not include right
            if nums[i] < pivot:
                # less than pivot, update low index, in left side
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
        # nothing update all left are larger than pivot
        nums[low], nums[right] = nums[right], nums[low] 
        return low

    
"""
SOLUTION4: sort with lambda function PASS
"""
ls = sorted(nums, key=lambda x: x, reverse=True)
return ls[k-1]
