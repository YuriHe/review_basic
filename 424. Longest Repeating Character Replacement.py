class Solution:
    """
    Question: longest repeating substring and can replace k times 
    sliding window
    window is valid repeating window
    ABAB, right = 3, right - left + 1 = 4 - max(char) <= k: valid window
    """
    def characterReplacement(self, s: str, k: int) -> int:
        # SOLUTION1 slide window O(n)
        count = [0] * 26
        left,right = 0, 0
        res = 0

        while right < len(s):
            # update count 
            idx = ord(s[right]) -ord('A')
            count[idx] += 1

            # handle invalid window
            while (right - left + 1) - max(count) > k:
                # move left of window
                idx = ord(s[left]) -ord('A')
                count[idx] -= 1
                left += 1
            
            # update valid result
            res = max(res, right - left + 1)
            right += 1
        return res










        