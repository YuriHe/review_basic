class Solution:
    """
    1.brute force O(m+n)
    merge two sorted array-> get one merged list, count len, if len is even, find index(len//2-1) and index(len//2) /2;
    if odd, index(len//2)
    """
    def mergesort(self, ls1, ls2):
        m,n = len(ls1), len(ls2)
        res = [None] * (m+n)
        i,j,k = 0,0,0
        while i < m and j <n:
            if ls1[i] < ls2[j]:
                res[k] = ls1[i]
                i+=1
            else:
                res[k] = ls2[j]
                j += 1
            k+=1
        while i < m:
            res[k] = ls1[i]
            i+=1
            k+=1
        while j < n:
            res[k] = ls2[j]
            j+=1
            k+=1
        return res

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1solution
        res = self.mergesort(nums1, nums2)
        print(res)
        
        if len(res) % 2 != 0: # odd
            # get middle index
            mid = len(res)//2
            return float(res[mid])
        else: # len is even
            mid1 = len(res) // 2 - 1
            mid2 = len(res) // 2
            
            return (res[mid1]+res[mid2]) /2