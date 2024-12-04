"""
1. Quicksort
TLE since all repeated 
Divide and conquer
T: O(nlogn) for best if use randomized pivot.  will be O(n*2) if use mid when repeated array[5,5,5] 
moodify input array in-place
find pivot use random, use mid
Partition the Array: Rearrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, 
and all elements greater than the pivot will be on its right. 
The pivot is then in its correct position, and we obtain the index of the pivot.
"""
def sortArray(self, nums: List[int]) -> List[int]:
    def divide(A, low, high):
        if low >= high: return
        p = partition(A, low, high)
        divide(A, low, p-1), 
        divide(A, p + 1, high)
    
    def partition(A, low, high):
        # swap median with pivot
        mid = (low + high) // 2
        A[high], A[mid] = A[mid], A[high]
        i = low - 1

        for j in range(low, high):
            if A[j] < A[high]: 
                i = i + 1
                A[i], A[j] = A[j], A[i]
                
        A[high], A[i+1] = A[i+1], A[high]
        return i + 1
    
    divide(nums,0,len(nums) - 1)
    return nums

"""
2. Bubble sort TLE
compare adjacent, swap adjacent, last one is always largest after one round sort
"""
def sortArray(self, nums: List[int]) -> List[int]:
    if not nums: return []

    for i in range(len(nums)):
        swap = False
        # i control rounds
        for j in range(0, len(nums)-i-1):  # skip last one, since j compare j+1
            if nums[j] > nums[j+1]:
                # swap
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swap = True
        # after cur round, nothing swap, exit early
        if not swap: 
            break
    return nums
    

"""
3.Merge sort
Divide and conquer T&S: O(nlogn)
recursion call to divide two array 
compare base case from left and right subarray
create new subarrays
"""
def sortArray(self, nums: List[int]) -> List[int]:
    if not nums: return []

    def merge(l, r):
        res = []
        i, j, m, n = 0, 0, len(l), len(r)
        while i < m and j < n:
            if l[i] <= r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        # additional len from l or r
        while i < m:
            res.append(l[i])
            i += 1
        while j < n:
            res.append(r[j])
            j += 1

        return res

    def divide(ls):
        # base case end cur recursion call
        if len(ls) <= 1:
            return ls
        # keep divide two parts recursively
        mid = len(ls) // 2
        l = ls[:mid]
        r = ls[mid:]
        lr = divide(l)
        rr = divide(r)
        # after recursion merge, be used to upper calls
        return merge(lr, rr)
    
    return divide(nums)


# Insertion Sort
"""
Insertion Sort is a simple sorting algorithm that move one element at a time, from left to right.
It works by repeatedly taking an element from the unsorted portion and inserting it into its correct position in the sorted portion of the list.

x <= pivot | pivot | unsort

Example 1:

Input:
pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]

Output:
[[(5, "apple"), (2, "banana"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")]]
Notice that the output shows the state of the array after each insertion. The last state is the final sorted array. There should be pairs.length states in total.
"""
# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    """
    Use two pointer, compare cur value to sorted array, if less then swap, continue 
    find smaller in sorted list(from right to left)
    T: O(n^2) for average&worst, O(n) for best
    """
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []
        
        for i in range(n):
            j = i - 1

            while j >= 0 and pairs[j+1].key < pairs[j].key:
                # swap with cur and continue find smaller in sorted list
                pairs[j+1], pairs[j] = pairs[j], pairs[j+1]
                j -= 1

            res.append(pairs[:])

        return res
        




