class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1SOLUTION: hashmap S&T:O(n)
        ctn = collections.Counter(nums1)
        res = []
        for n in nums2:
            if n in ctn:
                if ctn[n] > 0:
                    res.append(n)
                    ctn[n] -= 1
        return res
        # 2SOLUTION: two pointer T:nlogn S:1
        # sort, no extra handle since sorted and compare closet values
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j +=1 
            else:
               # intersection
               res.append(nums[i])
               i+=1
               j+=1
        return res
        # Followup1: What if the given array is already sorted? How would you optimize your algorithm?
        # Answer: 2nd solution is better. skip cost of sorting, time will be O(n)
        # Followup2: What if nums1's size is small compared to nums2's size? Which algorithm is better?
        # Answer: 1st solution is better. 
        # Followup3:  What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
        # Answer: 1st solution is better. Use nums1's hashmap, and sequentially load and process nums2 Or sub-range for both if both are oout of memory



        