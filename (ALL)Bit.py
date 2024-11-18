"""
67. Add Binary
"""
def addBinary(self, a: str, b: str) -> str:
    # SOLUTION1 python built function bin
    # convert binary to integer and sumup then convert integer to binary
    a_i = int(a, 2)
    b_i = int(b, 2)
    total = a_i + b_i
    return bin(total)[2:] # remove prefix '0b'

"""
190. Reverse Bits
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
        res |= n & 1
        # shift n to right to process next bit
        n >>= 1
    return res


"""
191. Number of 1 Bits
handle last bit from binary string: n%2(n canbe binary/int) or n&1
"""
def hammingWeight(self, n: int) -> int:
    # SOLUTION 1 built function
    binary_str = bin(n)[2:]
    ctn = 0
    for c in binary_str:
        if c == "1":
            ctn += 1
    return ctn

    # SOLUTION 1.1
    return bin(n).count('1')

    # SOLUTION2 shifting
    ctn = 0
    while n:
        # check if least significant bit is 1
        # also ok: ctn += n%2
        ctn += n&1
        # process next bit from n
        n >>=1
    return ctn


"""
Question: 136. Single Number
if same number, in bit side, will get 0 -> use XOR ^ operator
"""
def singleNumber(self, nums: List[int]) -> int:
    res = nums[0]
    for i in range(1, len(nums)):
        res ^= nums[i]
    return res


"""
137. Single Number II [5,5,5,7]
ones=0
twos=0
1 iter:
ones = 0^5&~0=5
twos= 0^5&~5=0
2 iter:
ones = 5^5&~0=0
twos =0^5&~0=5
3 iter:(all bits for 5 have been canceled oout)
ones= 0^5&~5=0
twos=5^5&~0=0

"""
def singleNumber(self, nums: List[int]) -> int:
    # hold bits seen once
    ones = 0
    # hold bits seen twice, if see third, will cleanup ones and twos
    twos = 0
    for n in nums:
        # Update 'ones' with bits that have been seen once, ignoring those in 'twos'
        ones = (ones ^ n) & ~twos
        # Update 'twos' with bits that have been seen twice, ignoring those in 'ones'
        twos = (twos ^ n) & ~ones

    return ones


"""
    338. Counting Bits
    Question: Bit manipulation
"""
def countBits(self, n: int) -> List[int]:
    res = [0] * (n+1)
    for i in range(1, n+1):
        res[i] = self.count1(i)
    return res
    
def count1(self, n):
    ctn = 0
    while n > 0:
        ctn += n & 1
        n >>= 1
    return ctn


"""
    1318. Minimum Flips to Make a OR b Equal to c
    A or B = C flip 0 or 1
"""
def minFlips(self, a: int, b: int, c: int) -> int:
    flips = 0
    while a > 0 or b > 0 or c > 0: # use or not and
        # extract least significant bit of a, b, c
        a_bit = a &1
        b_bit = b &1
        c_bit = c &1

        if c_bit == 1:
            if a_bit == 0 and b_bit == 0:
                flips +=1 # only one of them
        else:
            flips += (a_bit + b_bit)
        
        # shift right and check next bit
        a >>= 1
        b >>= 1
        c >>= 1
    return flips