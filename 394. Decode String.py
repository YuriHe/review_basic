class Solution:
    """
    Question: Decode String 
    Topic: stack
    TODO: insert all into stack except "]",  one round include digits[letters 
    """
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        for c in s:
            if c != "]":
                stack.append(c)
            else: # handle now []
                temp = ""
                # handle letter
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                # handle [
                if stack and stack[-1] == "[":
                    stack.pop()
                # handle digit
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                temp = int(num) * temp
                # now store this whole temp back to stack
                stack.append(temp)
        # now stack only letters, not digits and [
        for c in stack:
            res+= c
        return res


                
