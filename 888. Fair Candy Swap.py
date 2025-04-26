class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes)-sum(bobSizes)) //2
        for b in bobSizes:
            if diff + b in aliceSizes:
                return [diff+b, b]