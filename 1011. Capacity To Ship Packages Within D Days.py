class Solution:
    """
    Binary search
    set lo: max(weights) not 1 because must carry each package as whole cannot splitting it
    """
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            day = 1
            curSum = 0
            for w in weights:
                if curSum + w > cap:
                    day += 1
                    curSum = w
                else:
                    curSum += w
                if day > days:
                    return False

            return True

        # main part
        # lo, hi means capacity
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if canShip(mid):
                # it is valid already find less to get less 
                hi = mid
            else:
                lo = mid + 1
            
        return lo