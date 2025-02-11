class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        1.Solution:Stack
        Idea: push all char from string, check top [partlength], then pop in loop
        # """
        stack = []
        # store index to stack
        for c in s:
            stack.append(c)
            if len(stack) >= len(part):
                # check top if part
                # convert top part of stack to string
                tmp = "".join(stack[-len(part):])
                if tmp == part:
                    # pop for this substring from stack
                    for _ in range(len(tmp)):
                        stack.pop()
        return "".join(stack)

        """
        2.Solution:Dynamic modify string for delete all substring
        """
        while part in s:
            # Modify input s from delete part(substring)
            left_idx = s.find(part) # return -1 if not found
            s = s[:left_idx] + s[left_idx+len(part):]
        return s