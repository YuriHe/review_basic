""" 
121. Best Time to Buy and Sell Stock
    Question: find max diff from two different index (buy < sell)
    Solution1(BEST): native way T:O(n) S: O(1)
    Solution2: DP (find max/min and keep do recursion)T:O(n), S:O(n)
"""
def maxProfit(self, prices: List[int]) -> int:
    # Solution1:
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
    # Solution2: 
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


"""
    122. Best Time to Buy and Sell Stock II
    Question: accumulate profits from multiple transactions, sell index >= buy index
"""
def maxProfit(self, prices: List[int]) -> int:
    profit  = 0
    buy = prices[0]
    for i in range(1, len(prices)):
        if prices[i] > buy:
            profit += (prices[i] - buy)
        buy = prices[i]
    return profit

