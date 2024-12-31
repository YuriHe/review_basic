class Solution:
    """
    Question: return maximum sum for subarray at most k jump, j - i <= k
    Topic:Window + monotonic decreasing queue(largest=q[0])DP mark max sum at every index
    """
    def maxResult(self, nums: List[int], k: int) -> int:
    # Maximum sum for subarray at most k jump
    q = deque()
    # use dp store maximum score at each index
    dp = [float('-inf')] * len(nums)
    # initial default window
    dp[0] = nums[0]
    q.append(0)
    for i in range(1,len(nums)):
        # 1.maintain window
        while q and i - q[0] > k:
            q.popleft()
        # 2.compute max score
        dp[i] = max(dp[i], dp[q[0]] + nums[i])
        # 3.maintain decreasing queue
        while q and dp[i] >= dp[q[-1]]:
            q.pop()
        # 4.append
        q.append(i)
    return dp[-1]
        