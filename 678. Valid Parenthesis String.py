class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        1.Solution: stack
        Idea:if open bracket push to stack, count*, pop close bracket. if result *n && len(stack)<=(*n) or == 0 return true
        corner case (*)( -> false, need to consider index of * &(, so stack, star store index;
        Time: O(n) Space: O(n)
        """
        stack = []
        star = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == '*':
                star.append(i)
            else: # )
                if stack: # match ')' with '('
                    stack.pop()
                else:
                    if star: # match ')' with '*'
                        star.pop()
                    else: # no * to match ')'
                        return False
        
        # ***((( False, (*)( False
        while stack and star:
            # * must behind (
            if star[-1] > stack[-1]:
                stack.pop()
                star.pop()
            else:
                return False
        return len(stack) == 0


