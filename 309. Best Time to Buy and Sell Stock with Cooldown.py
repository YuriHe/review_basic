class Solution:
    """
    Question: max profit, buy and sell multiple transaction, 
    cooldown after sell(next one cannot do any)
    buy-sell-cooldown-rebuy
    """
    def maxProfit(self, prices: List[int]) -> int:
        """
        SOLUTION1: DP bottom-top
        STEP:analyze state (hold, sold, cool)
        hold[i] means max profit when hold stock at ith day
        sold[i] means max profit when sold at ith day
        cool[i] means max proodit when nothing no hold no action
        """
        if not prices: return 0

        # dp array
        n = len(prices)
        hold = [0] * n
        sold = [0] * n
        cool = [0] * n

        # default
        hold[0] = -prices[0] # first day buy stock
        sold[0] = 0          # first day cannot sell
        cool[0] = 0          # first day no action

        for i in range(1, n):
            # i-1 hold, i keep hold; i-1 cool, i buy
            hold[i] = max(hold[i-1], cool[i-1]-prices[i])
            # i-1 hold, i sell
            sold[i] = hold[i-1] + prices[i]
            # i-1 cool, i keep cool; i-1 sell, i cool
            cool[i] = max(cool[i-1], sold[i-1])
        
        return max(sold[n-1], cool[n-1])