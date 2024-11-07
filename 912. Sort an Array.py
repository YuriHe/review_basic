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
    def quicksort(A, low, high):
        if low >= high: return
        p = partition(A, low, high)
        quicksort(A, low, p-1), 
        quicksort(A, p + 1, high)
    
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
    
    quicksort(nums,0,len(nums) - 1)
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

    def merge(l: List[int], r: List[int]) -> List[int]: 
        res = []
        a, b = 0,0 
        while a < len(l) and b < len(r):
            if l[a] <= r[b]:
                res.append(l[a])
                a += 1
            else:
                res.append(r[b])
                b += 1
        
        while a < len(l):
            res.append(l[a])
            a+= 1

        while b < len(r):
            res.append(r[b])
            b +=1

        return res

    def mergesort(nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        l = nums[:mid]
        r = nums[mid:]

        # recursion top to bottom(base case)
        l = mergesort(l)
        r = mergesort(r)
        
        # merge from base case (base case can easily sort)
        return merge(l, r)

    return mergesort(nums)
    