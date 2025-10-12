class Solution:
    """
    121. Best Time to Buy and Sell Stock
    Question: buy and sell one time transaction, buy cannot have same day as sell 
    """
    def maxProfit(self, prices: List[int]) -> int:
        """
        SOLUTION1: iterate array
        STEP:if find lower price than buy, update buy, every step will check profit
        """
        if len(prices) <= 1: return 0
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] >= buy:
                profit = max(profit, prices[i]- buy)
            else:
                # cur price is lower than buy, update buy
                buy = prices[i]
        return profit


class Solution:
    """
    122. Best Time to Buy and Sell Stock II
    Question: accumulate transactions, best can have same day as sell
    """
    def maxProfit(self, prices: List[int]) -> int:
        """
        SOLUTION1: iterate array
        STEP: update buy if find lower, if have profit, then accumulate it
        """
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > buy:
                profit += (prices[i]-buy)
            
            # each time update buy since accumulate profit
            buy = prices[i]
        return profit
        
