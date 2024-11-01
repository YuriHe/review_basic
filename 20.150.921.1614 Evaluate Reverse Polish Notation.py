"""
    20. Valid Parentheses
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



import math
class Solution:
    """
    150. Evaluate Reverse Polish Notation
    Question:
    1.understand reverse posh notion
    2.insert num to stack, second_pop + operator + first_pop
    """
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for v in tokens:
            if len(stack) >= 2 and v in "+-*/":
                pop1 = stack.pop()
                pop2 = stack.pop()
                if v == "+":
                    stack.append(pop1+pop2)
                elif v == "-":
                    stack.append(pop2-pop1)
                elif v == "*":
                    stack.append(pop2*pop1)
                elif v == "/":
                    if pop2 / pop1 < 0:
                        stack.append(math.ceil(pop2/pop1))
                    else:
                        stack.append(math.floor(pop2/pop1))
            else:
                stack.append(int(v))
        return stack[-1]


class Solution:
    """
    921. Minimum Add to Make Parentheses Valid
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
        

class Solution:
    """
    1614.Maximum Nesting Depth of the Parentheses
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
                    if len(stack) > res: # function like res = max(res, len(stack))
                        # update res,since s is vps
                        res = len(stack)
                    stack.pop()
        return res
