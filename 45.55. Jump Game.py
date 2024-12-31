"""
    55. Jump Game
    Question: Check if farthest step to reach last index of array
    Greedy algorithm
"""
def canJump(self, nums: List[int]) -> bool:
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


