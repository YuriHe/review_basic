"""
    Question: handle pairs of () [] {}
    Topic: Stack
    TODO: see left brackets, store into stack; otherwise pop out
"""
def isValid(self, s: str) -> bool:
    stack = []
    for c in s:
        if c == "(" or c == "{" or c == "[":
            stack.append(c)
        else:
            if len(stack) == 0: return False
            if (c == ")" and stack[-1] == "(") or (c == "]" and stack[-1] == "[") or (c == "}" and stack[-1] == "{"):
            # remove last element from stack list
                stack.pop()
            else: return False
    return len(stack) == 0
