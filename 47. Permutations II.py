class Solution:
    """
    Question:all permutation which input may duplicate [1a,1b,2a], 1a must before 1b
    Step:Sort,Verify i > 0 and nums[i] == nums[i-1] and not visit[i-1])
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        visit = [False] * len(nums)
        nums.sort()

        def bt(inner):
            # base case
            if len(inner) == len(nums):
                res.append(inner[:])
                return
            # recursion
            for i in range(len(nums)):
                if visit[i] or (i > 0 and nums[i] == nums[i-1] and not visit[i-1]):# 1a not before 1b, so 1a will occur after 1b
                    continue
                visit[i] = True
                inner.append(nums[i])
                bt(inner)
                visit[i] = False
                inner.pop()

        bt([])

        return res


