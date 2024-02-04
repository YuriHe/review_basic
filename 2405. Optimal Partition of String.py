"""
    Question: return minimum number of substring in which all chars are unique
    Topic: use sliding window + map
"""
def partitionString(self, s: str) -> int: 
    # only lowercase
    window_count = [0] * 26
    i, j,res = 0, 0, 1
    while j < len(s):
        # count freq
        window_count[ord(s[j]) - ord('a')] += 1
        if window_count[ord(s[j]) - ord('a')] > 1:  # duplicate
            res += 1
            while i < j:
                # clean window
                window_count[ord(s[i]) - ord('a')] -= 1
                i += 1  # increment i
        j += 1  # increment j

    return res