class Solution:
    """
    Question: string compression
    Two pointer, no need flag, but handle len(chars)+1 to add last group
    """
    def compress(self, chars: List[str]) -> int:
        if not chars: return 0
        i = 0 # return new length of chars
        ctn = 1 # number of char in current group

        for j in range(1, len(chars)+1):
            if j < len(chars) and chars[j] == chars[j-1]: # in same group
                ctn += 1
            else:
                # handle old group (char + digits)
                chars[i] = chars[j-1]
                i += 1
                if ctn > 1:
                    for c in str(ctn):
                        chars[i] = c
                        i += 1
                # start new group
                ctn = 1
        
        return i


