"""
    55. Jump Game
    Question: Check if farthest step to reach last index of array
    Greedy algorithm
"""
def canJump(self, nums: List[int]) -> bool:
    # 1 SOLUTION: Greedy(best)
    # value in array represent max jump length
    # only farther reach, no need dp array
    far = 0
    for i in range(len(nums)):
        # Must here
        if far < i: # farthest still less than i
            return False
        far = max(far, i + nums[i])
        if far >= len(nums)-1:
            return True
    return False            

def canJump(self, nums: List[int]) -> bool:
        # 2SOLUTION: 1DP
        # [0] return True
        # only one ele no need jump
        if len(nums) <= 1: return True

        # farthest jump at i, mark farhtest index
        dp = [0] * len(nums)
        # default 
        dp[0] = nums[0]

        for i in range(1, len(dp)):
            # update farthest
            # make sure if farthest >= i
            if dp[i-1] < i:
                return False
            else:
                dp[i] = max(dp[i-1], i + nums[i])

        return dp[-1] >= len(nums)-1
"""
    45. Jump Game II
    Question: Minimum number of jumps to reach last index 
    Think Greedy
    Each jump will have rightmost border, hit border, need more jumps
    Greedy
    T: O(n)
    S: O(1)
"""
def jump(self, nums: List[int]) -> int:
    if len(nums) <= 1: 
        # no jump
        return 0
    # cur_end is right border of jump
    # far is currently far reach
    total, cur_end, far = 0,0,0
    for i in range(len(nums)):
        far = max(far, nums[i] + i)
        if i == cur_end: # reach right border need one more jump, update right border
            total+=1
            cur_end = far 
        if cur_end >= len(nums)-1: # exit earlier
            break
    return total


