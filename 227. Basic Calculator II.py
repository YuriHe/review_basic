class Solution:
    """
    Question: return number when use basic calculator, number is >=0
    Followup:number can be negative
    """
    def calculate(self, s: str) -> int:
        """
        SOLUTION1: Stack
        STEP1:don't push num immediately to stack, when see op then push or posh
        TIME: O(n) SPACE:O(n)
        """
        stack = []
        op,v = "+", 0 # default 
        for i, c in enumerate(s):
            if c.isdigit(): # many more digits 32
                v = v * 10 + int(c)
            if c in "+-*/" or i == len(s)-1:
                if op == "+":
                    stack.append(v)
                elif op == "-":
                    stack.append(-v)
                elif op == "*":
                    stack.append(stack.pop() * v)
                elif op == "/":
                    # wrong since -5/2=-3, should -2
                    # stack.append(stack.pop() // v)
                    # int(-3/2)=-1
                    stack.append(int(stack.pop() / v))
                
                # update op
                op = c
                # reset v afte op change
                v = 0 

        return sum(stack)

