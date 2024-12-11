class Solution:
    """
    Question: minimize the largest sum of subarray after k times split
    the possible range of sum is [max(nums), sum(nums)]
    Guess -> binary search, find minimal possible value of largest sum,
    given guess max_sum, is it possible to split array into non empty subarray with at most k times
    if not, max_sum too smaller; if yes, try another smaller guess
    helper: valid
    time: O(nlogn)
    """
    def splitArray(self, nums: List[int], k: int) -> int:
        def valid(maxSum):
            # given maxSum(possible result), see if possible when at most k split(cut)
            cut, curSum = 1, 0
            for n in nums:
                curSum += n
                if curSum > maxSum:
                    # need more cut
                    cut += 1
                    # reset sum
                    curSum = n
            return cut <= k

        # main part
        # before use binary search, defind pointer
        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low+high) // 2
            if valid(mid):
                high = mid
            else:
                low = mid + 1
        return low # minmum largest sum

        
        
