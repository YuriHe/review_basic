"""
    Question: Read string, return [number of lines needed, width of pixels in last lined]
    Input width len = 26 for 26 lowercase letters 
    each line won't longer than 100pixel
    """
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        presum = 0
        line = 1

        for i in range(len(s)):
            c = s[i]
            idx = ord(c) - ord("a")
            width = widths[idx]
            if presum  + width > 100:
                line += 1
                # go to next line
                presum = width
            else:
                presum += width
        return [line, presum]