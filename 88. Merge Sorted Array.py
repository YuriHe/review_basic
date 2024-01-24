def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    Question: merge two sorted array in-place
    Topic: Two pointer, use longest array as res
    Issue: which longer doesn't matter, starting from back
    """
    k, i, j = m+n-1, m-1, n-1
    # when m =n case:
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    # only rest of m
    while i >= 0:
        nums1[k] = nums1[i]
        i -= 1
        k -= 1
    # only rest of n
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    