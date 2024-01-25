"""
    Question: find max diff from two different index (buy < sell)
    Solution1: brute force T:O(n^2) TIMOUT!!
    Solution2(BEST): native way T:O(n) S: O(1)
    Solution3: DP (find max/min and keep do recursion)T:O(n), S:O(n)
"""
def maxProfit(self, prices: List[int]) -> int:
    # Solution1: fail
    if len(prices) <= 1: return 0
    res = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            res = max(res, prices[j] - prices[i])
    return res
    # Solution2:
    if len(prices) <= 1: return 0
    res = 0
    buy = prices[0]
    for i in range(1, len(prices)):
        if prices[i] > buy:
            res = max(res, prices[i]-buy)
        else:
            # find lower price
            buy = prices[i]
    return res
    # Solution3: 
    # create new arr for store profit at that point
    if len(prices) <= 1: return 0
    dp = [0] * len(prices)
    # initial val
    buy = prices[0]
    res = 0
    for i in range(1, len(prices)):
        # each in dp means profit from buy and sell at i
        dp[i] = max(prices[i] - buy, 0)
        if prices[i] < buy:
            # find lower price, reset buy
            buy = prices[i]
        res= max(res, dp[i])
    return res
