class Solution:
    """
    QUESTION: find max x after at most t times, x can +/- 1, num can +/- 1
    HOW: to maximize final x,
     we can 1.increase x directly, gaining t
            2.use all t operations, decrease num then add num to x
    """
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2*t
        