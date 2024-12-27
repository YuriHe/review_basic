class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Q: find minimum distance between each two balls, when m larger, distance smaller, monotonically decrease
        # sort position index doesn't matter
        position.sort()
        
        def valid(minD):
            # abs(x-y) 
            # compare neighbor
            ctn, flag= 1, position[0] # put first ball in first index, ctn is ball
            for i in range(1, len(position)):
                if position[i]- flag >= minD:
                    # put one ball
                    ctn += 1
                    # update for new ball
                    flag = position[i]
                    # prune, exit early
                    if ctn >=m: return True
            return False

        # define distance low, high
        low, high = 0, position[-1] - position[0]
        while low < high:
            mid = high - (high-low) // 2
            if valid(mid):
                # valid ball count >= m, try distance larger
                low = mid
            else: # valid ball count < m, try distance smaller
                high = mid - 1
        return low 

        