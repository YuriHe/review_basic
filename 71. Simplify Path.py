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

    # 2 way
    def simplifyPath(self, path: str) -> str:
        # string pattern/rule
        # stack
        # split / delimiter convert str to list 
        stack = []
        arr = path.split("/")
        # remove all fasly in arr
        ls = list(filter(None, arr))
        for w in ls:
            if w == ".":
                continue
            elif w == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(w)
        return "/" + "/".join(stack)

