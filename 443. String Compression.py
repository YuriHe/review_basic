class Solution:
    """
    Question: string compression
    Two pointer, no need flag, but handle len(chars)+1 to add last group
    """
    def compress(self, chars: List[str]) -> int:
        ctn = 1
        k = 0

        for i in range(1, len(chars)+1): 
            # iterate last+1 to avoid duplicate code(cur part+last part)
            # handle boundary 
            if i < len(chars) and chars[i] == chars[i-1]:
                   ctn += 1
            else: # outbound or diff group go through
                # new section
                chars[k] = chars[i-1]
                k+=1
                if ctn > 1:
                    for d in str(ctn):
                        chars[k] = d
                        k+=1
                # reset
                ctn = 1

        return k

        # 2 SOLUTION: redundant but native
        def compress(self, chars: List[str]) -> int:
            ctn = 1
            k = 0

            for i in range(1, len(chars)):
                if chars[i] != chars[i-1]:
                    # new section
                    chars[k] = chars[i-1]
                    k+=1
                    if ctn > 1:
                        tmp = ctn
                        tmp2 = ""
                        for d in str(tmp):
                            chars[k] = d
                            k+=1

                    # reset
                    ctn = 1
                else:
                    # same 
                    ctn += 1
            # last
            chars[k] = chars[-1]
            k+=1
            if ctn > 1:
                tmp2 = ""
                for d in str(ctn):
                    chars[k] = d
                    k += 1

            return k