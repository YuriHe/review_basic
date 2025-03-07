class Solution:
    """
    190. Reverse Bits
    Reverse in 10base, 2base, bit operator
    Think 10base integer 342
    ans = ans*10 + n%10(last digit)
    n//=10
    Think 2base
    ans = ans*2 + n%2
    n//=2
    Think bit
    anw = <<=1(shift left) + n&1(last bit)
    n>>=1(shift right)
    Simulation: 32 bit reprensation: n=13
    res=00000000000000000000000000000000
    n=00000000000000000000000000001101
    1.res <<= 1, res=00000000000000000000000000000000
    2.res |= n & 1, n&1 isolate last bit of n, which 1 since 13 in binary end in 1, res=00000000000000000000000000000001
    3.n >> =1, n become 6, n=00000000000000000000000000000110
    """
    def reverseBits(self, n: int) -> int:
        
        res = 0 
        # loop all 32 bits
        for i in range(32):
            # shift res left by 1 to make room for next bit
            res <<= 1
            # add least significant bit of n to res
            # last bit of n is 1, then set last bit oof res to 1 otherwise unchange
            res += n&1
            # shift n to right to process next bit
            n >>= 1
        return res