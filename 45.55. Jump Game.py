"""
    55. Jump Game
    Question: Check if farthest step to reach last index of array
    Greedy algorithm
"""
def canJump(self, nums: List[int]) -> bool:
    far = 0
    for i in range(len(nums)):
        if far >= len(nums) - 1: return True
        far = max(far, nums[i]+i)
        if nums[i] == 0 and far <= i:
            return False
    return False
    
"""
    45. Jump Game II
    Question: Minimum number of jumps to reach last index 
    Think BFS, layer by layer, here is section(include right border)
    Each jump will have rightmost border, hit border, need more jumps
    Greedy
    T: O(n)
    S: O(1)
"""
def jump(self, nums: List[int]) -> int:
    total = 0 # minimum jmps
    r = 0 # cur right border of jump
    far = 0 # farthest position from cur jump

    for i in range(len(nums)-1): # last second end jump, last is dest
        # update farthest point that can be reached from cur position
        far = max(far, nums[i] + i)

        if i == r: # reach right border, need 1 jump
            total += 1
            # update new right border
            r = far

            # check if right border reach end
            if r >= len(nums) - 1:
                break
    
    return total


