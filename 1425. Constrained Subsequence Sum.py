# subsequence sum ,not prfix, use dp (BETTER)
# create dp dp[i] means maximum  sum
# each val in dp is sum(at least)
dp = nums[:]
res = float('-inf')
q = deque()

for i in range(len(nums)):
    # move left remove index out of sliding window of k
    if q and i - q[0] >k:
        q.popleft()
    # update dp[i] using maximum value in q
    if q:
        dp[i] = max(dp[i], dp[q[0]]+nums[i]) # only here use nums[i]
    # move right, keep decreasing queue
    while q and dp[i] >= dp[q[-1]]:
        q.pop()
    # valid
    res = max(res, dp[i])
    # push to q
    q.append(i)
return res 

    # careful window size 
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # subsequence sum ,not prfix, use dp
        # create dp dp[i] means maximum  sum
        # each val in dp is sum(at least)
        dp = nums[:]
        res = float('-inf')
        q = deque()
        
        for i in range(len(nums)):
            # 1.取值update dp[i] using maximum value in q
            # 这dp值要给下一次用
            if q:
                dp[i] = max(dp[i], dp[q[0]]+nums[i]) # only here use nums[i]
            res = max(res, dp[i])
            # 2.left side pop window
            if q and i - q[0] >=k:
                q.popleft()
            # 3.move right, keep decreasing queue
            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            # 4.进 push to q
            q.append(i)
        return res 