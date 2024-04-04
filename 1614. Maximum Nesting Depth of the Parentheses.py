class Solution:
    """
    Question: Valid parentheses string, Assume s is VPS
    TOPIC: stack
    ISSUE: s already VPS, find maxdepth((2)+((3)))->3
    """
    def maxDepth(self, s: str) -> int:
        stack = []
        res = 0
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if c == ")":
                    if len(stack) > res:
                        # update res,since s is vps
                        res = len(stack)
                    stack.pop()
        return res
