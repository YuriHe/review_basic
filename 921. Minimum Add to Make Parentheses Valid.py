class Solution:
    """
    Question:  Minimum Add to Make Parentheses Valid
    TOPIC: valid parenthese -> stack
    """
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if len(stack) == 0:
                    # add open bracket
                    res += 1
                else:
                    stack.pop()
        return len(stack) + res
        