class Solution:
    """
    Question: dynamic array
    handle value at index
    compared prices can be used multiple times
    1 Solution: brute force O(n^2)
    2 Solution: stack handle element comparison at diff index
    """
    def finalPrices(self, prices: List[int]) -> List[int]:
        # SOLUTION1
        for i in range(len(prices)):
            cur = prices[i]
            for j in range(i+1, len(prices)):
                compared = prices[j]
                if compared<= cur: # discount exit
                    prices[i] = cur - compared
                    break
        return prices

        # SOLUTION2
        stack = []
        for i, p in enumerate(prices):
            # compared prices can be used multiple times
            while stack and prices[stack[-1]] >= p:
                # update value from top index in stack
                prices[stack.pop()] -= p
            stack.append(i)

        return prices