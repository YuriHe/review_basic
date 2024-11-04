class Solution:
    """
    Question: generate combination of valid parentheses from n pairs
    Use recursion/backtrack, ( and ) are have n times to use.
    For valid combination of parentheses, open must use >= close; aks open left <= close
    """
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(cur, ope, close):
            # open left more than close, it is invalid
            if close < ope: return
            if ope == 0 and close == 0:
                res.append(cur)
                return

            if ope > 0:
                helper(cur+"(", ope-1, close)
            if close > 0:
                helper(cur+")", ope, close-1)
            

        helper("", n, n)
        return res