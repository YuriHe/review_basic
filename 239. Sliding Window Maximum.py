from collections import deque
class Solution:
    """
    Question;
    1.brute force nested loop find max for every window [i: i+k] and max
    2.monotonically decreasing queue, matain decreasing, if find cur larger than last, pop all 
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # Keep decreasing queue [larger, smaller]
    # Result size is N - windowsizeK + 1(simulate)
    res = []
    # q store i
    q = deque([])
    for i in range(len(nums)):
        # 1step: left side pop from q, maintain window size is K-1
        if q and i - q[0] > k-1: # or > k-1
            q.popleft()
        # 2step: right side pop from q, keep monotonically decreasing queue
        while q and nums[i] >= nums[q[-1]]:
            # pop all from q
            q.pop()
        q.append(i)
        if i >= k-1: # meet window size
            res.append(nums[q[0]])

        return res

            
