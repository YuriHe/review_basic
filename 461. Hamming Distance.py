class Solution:
    """
    2220. Minimum Bit Flips to Convert Number
    """
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        ctn = 0
        while diff:
            ctn += diff & 1
            diff >>= 1
        return ctn