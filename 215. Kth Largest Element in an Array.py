# """
#     Question: find Kth largest element from list
#     Topic: Minheap(PQ)!(NOT MAX HEAP) use size k, smallest of k largest eles on top
# """
def findKthLargest(self, nums: List[int], k: int) -> int:
    # SOLUTION1: minheap(default)
    # build O(n) heapify(nlogn)
    # create heap list 
    heap = []
    # build heap with k size and heapify O(nlogn)
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
    

# SOLUTION2: Quicksort-quickselect only recur kth largest
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

    
        
