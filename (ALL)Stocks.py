class Solution:
    """
    714. Best Time to Buy and Sell Stock with Transaction Fee
    Question: buy&sell stock
    DP - bottom up
    """
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices: return 0
        # maximum profit if not holding after ith day
        dp_no_hold = 0
        # maximum profit if holding after ith day
        dp_hold = -prices[0]

        for i in range(1, len(prices)):
            # update dp_no_hold, sell ith if hold
            dp_no_hold = max(dp_no_hold, prices[i] + dp_hold - fee)
            # update dp_hold, keep stock or buy
            dp_hold = max(dp_hold, dp_no_hold-prices[i])
        
        return dp_no_hold