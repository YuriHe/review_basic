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
    visited = [False] * len(nums)
    cur = [] # push/pop 
    def helper(index):
        # base case
        if len(cur) == len(nums):
            # done one round permutation, copy cur list
            res.append(cur[:])
            return
        for i in range(len(nums)):
            if visited[i]:
                continue # picked
            visited[i] = True
            cur.append(nums[i])
            helper(index+1)
            cur.pop() # use pop instead of remove
            visited[i] = False
    helper(0) # remember call recursion

    return res