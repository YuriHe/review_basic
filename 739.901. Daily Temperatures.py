class Solution:
    """
    739. Daily Temperatures
    Question: return days bigger than current value
    monotonic stack. find first greater element that mean need maintain stack is decreasing order 
    STEP:create stack store index. If cur > stack[-1] pop and mark res
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures: return []

        stack = [] # store idx which value in decreasing order 
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while len(stack) > 0 and t > temperatures[stack[-1]]: # stack store idx!
                top = stack.pop()
                res[top] = i - top
            stack.append(i)

        return res


"""
901. Online Stock Span
Question: return maximum number of consecutive days start from today and going backward <= cur price
Monotonic stack, store value decreasing order 
"""
class StockSpanner:

    def __init__(self):
        self.stack = [] # store (price, span)

    def next(self, price: int) -> int:
        day = 1 # itself
        while len(self.stack) > 0 and price >= self.stack[-1][0]:
            (_, span) = self.stack.pop()
            day += span

        self.stack.append((price, day))
        return day

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)