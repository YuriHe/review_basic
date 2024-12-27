class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m*k: return -1
        def validDay(maxD):
            flowers, bou = 0,0
            for d in bloomDay:
                if d <= maxD:
                    flowers += 1
                    if flowers == k: # adj meets
                        bou += 1
                        # rest for next bouquet
                        flowers = 0
                else:
                    # invalid 
                    flowers = 0
                # prune exit early
                if bou == m:
                    return True

            return False

        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            mid = (low+high) // 2 # maxDay
            if validDay(mid):
                high = mid
            else:
                low = mid + 1
        # minimum valid day finaly check
        return low if validDay(low) else -1