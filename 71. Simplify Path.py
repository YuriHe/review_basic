class Solution:
    """
    Question: simplify path
    1. use "/" delimiter and filter empty ""
    2. see .., then pop if stack not empty
    3. see . skip, see ..., .... valid 
    Use stack
    """
    def simplifyPath(self, path: str) -> str:
        ls = path.split("/")
        stack = []

        for c in ls:
            if c == "..":
                if len(stack) > 0:
                    stack.pop()
            elif c == "." or c == "":
                continue
            else:
                stack.append(c)
     
        return "/" + "/".join(stack)

