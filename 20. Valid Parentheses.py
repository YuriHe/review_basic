"""
    Question: handle pairs of () [] {}
    Topic: Stack
    TODO: see left brackets, store into stack; otherwise pop out
"""
def isValid(self, s: str) -> bool:
    stack = []
    for c in s:
        if c == "(" or c == "[" or c == "{":
            stack.append(c)
        else: # it is close bracket
            if len(stack) <= 0:
                return False

            # False scenario will be boarder
            if (c == "]" and stack[-1] == "[") or (c == "}" and stack[-1] == "{") or (c == ")" and stack[-1] == "("):
                stack.pop()
            else:
                return False # no match bracket
        
    return len(stack) == 0