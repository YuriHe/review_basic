"""
    Permute number, order does matter. O(n!factorail)
    all results are in fixed size
    Original list of elements: [1, 2, 3]
    All permutations:
    [1, 2, 3]
    [2, 1, 3]
    [2, 3, 1]
    [1, 3, 2]
    [3, 1, 2]
    [3, 2, 1]
    result have 6, 3! because 1*2*3
"""
def permute(self, nums: List[int]) -> List[List[int]]:
    res = []
    visit = [False] * len(nums)

    def bt(inner):
        if len(inner) == len(nums):
            res.append(inner[:])
            return 

        for i in range(len(nums)):
            if visit[i]:
                continue
            visit[i] = True
            inner.append(nums[i])
            bt(inner)
            inner.pop()
            visit[i] = False

    bt([])
    return res