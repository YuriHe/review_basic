"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.
k is slot, num range is 1 to n
"""
def combine(self, n: int, k: int) -> List[List[int]]:
    if k > n: # slot num more than number of n mean no empty combination
        return []
    res = []
    cur = []
    def helper(index):
        if len(cur) == k: 
            res.append(cur[:])
            return
        for i in range(index, n+1):  # start from index
            cur.append(i)
            helper(i+1)
            cur.pop()


    # call recursion
    helper(1)
    return res