class Solution:
    """
    Question:return decode string 
    Stack
    1.store all char excpet ]. [ use to separate blocks
    2.see ], tmp to get str pop from while loop until find [, then push whole str back to stack
    3.see num, then pop str * num -> update res 
    4.stack will modify to final string format
    """
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        for c in s:
            if c == "]":
                # close cur block[str]
                substr = ""
                while len(stack) > 0 and stack[-1] != "[":
                    substr = stack.pop() + substr
                # pop [
                stack.pop()
                # handle count
                ct = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    ct = stack.pop() + ct
                # decode this block
                substr = int(ct) * substr
                # push back to stack
                stack.append(substr)
            else:
                stack.append(c)

        return "".join(stack)