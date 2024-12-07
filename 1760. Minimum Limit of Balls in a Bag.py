class Solution:
    """
    Question:
    intuitive solution: PQ, find max, how to divide, will try all combination -> check input contraint, no guide
    binary search
    eg.[10]
    if penalty:1 -> (10-1) / 1 = 9times op
    if penalty:2 -> (10-1) / 2 = 4times op. use floor
    if penalty:3 -> (10-1) / 3 = 3times op

    guess penalty you want and consider maxop as well
    higher penalty less op times
    """
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(penalty):
            op = 0
            for n in nums:
                op += (n - 1) // penalty
            return op <= maxOperations
        
        low, high = 1, max(nums)
        while low < high:
            mid = (low + high) // 2
            if check(mid):
                # it works, move left, try to find smaller if possible
                high = mid
            else:
                low = mid + 1
        return low 

