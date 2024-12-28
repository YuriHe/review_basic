class Solution:
    """
    remove duplicatre and keep order 
    find smaller letter push 
    same as 1081. Smallest Subsequence of Distinct Characters
    """
    def removeDuplicateLetters(self, s: str) -> str:
        # mark char last occur
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        # mark visit
        visit = set()
        stack = []
        for i, c in enumerate(s):
            if c in visit:
                continue
            while stack and c < stack[-1] and last[stack[-1]] > i: # top of stack will occur again later 
                top = stack.pop()
                visit.remove(top)
            stack.append(c)
            visit.add(c)
        
        return "".join(stack)
        
