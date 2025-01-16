class Solution:
    """
    Question: return integer number that result of XOR of each integer in n1 ^ every integer in n2
    """
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # 1solution: brute force (TLE) n^2
        # res = 0
        # for n in nums1:
        #     for n2 in nums2:
        #         res ^= n ^ n2
        # return res
        # 2solution
        # use n1,n2,n3,   m1,m2,m3 to simulate. even&even|even&odd|.... -> found consider odd
        n1 = 0
        for n in nums1:
            n1 ^= n
        n2 = 0
        for n in nums2:
            n2 ^= n
        res = 0
        if len(nums1)% 2 != 0:
            res ^= n2
        if len(nums2) % 2 != 0:
            res ^= n1
        return res


