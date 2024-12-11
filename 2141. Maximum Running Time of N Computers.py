class Solution:
    """
    Question:
    guess maximum minutes
    binary search -> low = 0, high =sum(batteries)//n
    key points:
    1.If cannot run simultaneously for t1 , then they cannot run simultaneously for t2
    2.use binary search to find maximal running time, given guess time, if not, guess smaller
    3.handle all PC, so can sum(batteries) // n found the bound
    """
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def valid(time):
            # if given time, see if can run all PC n*time needed, if curSum >= n*time:yes
            curSum = 0
            for t in batteries:
                curSum += min(t, time)
                
            return curSum >= n * time

        # main part
        low, high = 0, sum(batteries)//n # mean maximum minute
        while low <= high:
            mid = (low+high) // 2
            if valid(mid):
                # cur is valid, go further if possible
                low = mid + 1
            else:
                high = mid - 1
        return high

            
