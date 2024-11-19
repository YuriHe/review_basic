class Solution:
    """
    Question: 39.Combination Sum
    pick number from candidates unlimited number of times. sum up to target
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, total, inner):
            # base case
            if total == target:
                res.append(inner[:])
                return
            # invalid case
            if total > target or idx == len(candidates):
                return 
            
            for i in range(idx, len(candidates)):
                inner.append(candidates[i])
                dfs(i, total + candidates[i], inner)
                inner.pop()

        dfs(0, 0, [])
        return res


class Solution:
    """
    216. Combination Sum III
    Question: use k number can select from 1 to 9, and sum up to n, each number used at most once
    dfs with backtracking
    """
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(num, total, inner):
            # base case 
            if len(inner) == k and total==n:
                res.append(inner[:])
                return 
            # invalid prune path
            if len(inner) >= k or total > n:
                return 

            # explore number from num to 9
            for i in range(num, 10):
                # handle cur val 
                inner.append(i)
                # search next one
                dfs(i+1, total+i, inner) # pass total+i in dfs, not write it separate
                # backtrack to try another combination
                inner.pop()

        dfs(1,0,[])
        return res