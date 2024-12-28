class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # get smallest integer after removing k digits
        # remove most significant position 
        # keep same digit, push smaller
        # if k still have removee last k digit
        stack = []
        for n in num:
            while stack and int(n) < int(stack[-1]) and k > 0:
                stack.pop()
                k-= 1
            stack.append(n)
        if k > 0:
            stack = stack[:len(stack)-k] # remove last k values
        res = ""
        zero = True
        for n in stack:
            if n == "0" and zero:
                continue
            else:
                zero = False
                res += n

        return res if res else "0"
        