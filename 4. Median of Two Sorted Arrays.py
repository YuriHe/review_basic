class Solution:
    """
    1.brute force O(m+n)
    merge two sorted array-> get one merged list, count len, if len is even, find index(len//2-1) and index(len//2) /2;
    if odd, index(len//2)
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1solution
        m,n = len(nums1), len(nums2)
        k, i, j = m+n-1, m-1, n-1
        res = [None] * (m+n)
        # handle value if exist in both nums1 and nums2:
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                # fill value of nums1 to index k
                res[k] = nums1[i]
                # move i index
                i -= 1
            else:
                # fill value of nums2 to index k
                res[k] = nums2[j]
                # move j index
                j -= 1
            # move k index
            k -= 1
        # only rest of m
        while i >= 0:
            res[k] = nums1[i]
            i -= 1
            k -= 1
        # only rest of n
        while j >= 0:
            res[k] = nums2[j]
            j -= 1
            k -= 1
        # now nums1 is final
        if len(res) % 2 != 0: # odd
            # get middle index
            mid = len(res)//2
            return float(res[mid])
        else: # len is even
            mid1 = len(res) // 2 - 1
            mid2 = len(res) // 2
            return (res[mid1]+res[mid2]) /2