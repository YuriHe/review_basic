class Solution:
    """1732. Find the Highest Altitude
    Question: prefix sum starting from 0
    """
    def largestAltitude(self, gain: List[int]) -> int:
        res = gain[0]
        prefix = gain[0]
        for i in range(1, len(gain)):
            prefix += gain[i]
            res = max(res, prefix)
        
        return res if res > 0 else 0