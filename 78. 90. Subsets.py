class Solution:
    """
    78. Subsets
    T: O(n^2)
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def bt(inner,idx):
            res.append(inner[:])
            for i in range(idx, len(nums), 1):
                inner.append(nums[i])
                bt(inner,i+1)
                inner.pop()

        bt([],0)
        return res

class Solution:
    """
    90. Subsets II
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # handle duplicate
        nums.sort()
        
        def bt(inner,idx):
            res.append(inner[:])
            for i in range(idx, len(nums), 1):
                if i != idx and nums[i] == nums[i-1]: # simulate the subset tree it happend [1,2] pop 2, i=1,go to i=2
                    continue
                inner.append(nums[i])
                bt(inner,i+1)
                inner.pop()

        bt([],0)
        return res