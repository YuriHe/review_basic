class Solution:
    """
    Question: find substring based on pattern/rules
    """
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        zero, one, res = 0, 0, 0

        for c in s:
            if c == "0":
                if one: # need to clean previous section if one > 0
                    # reset zero and one
                    zero = 0
                    one = 0
                zero += 1
            else:
                one += 1
                res = max(res, min(zero, one) * 2) # ensure equal zero and one

        return res
