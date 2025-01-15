class Solution:
    """
    Question: Return X which ^ N1 is smallest and count1(X)=count1(N2)
    If count1(N1) > count1(N2), remove extra set bits, for X^N1, so flip 1 to 0 starting from least significant position
    make higher keep same
    If count1(N1) < count1(N2), add more set bits
    """
    def minimizeXor(self, num1: int, num2: int) -> int:
        # count number of set bits(1s)
        def countBit(n):
            res = 0
            while n > 0:
                res += n & 1
                n >>= 1
            return res

        ctn1, ctn2 = countBit(num1), countBit(num2)
        x = num1
        i = 0
        # set bit is more in num1 remove least significant
        while ctn1 > ctn2:
            # check if ith bit in x is set
            # 1<<0:0001(1), 1<<1:0010(2); 1<<2:0100(4)
            if x & (1<< i):
                ctn1 -= 1
                # if ith bit in x truly set, flip bit to 0
                x ^= (1<<i)
            i+=1

        # no enough set bits in num1, add least significant
        while ctn1 < ctn2:
            # check ith bit in x unset(0)
            if x & (1<<i) == 0:
                ctn1 += 1
                # if ith bit in x truly unset, flip bit to 1
                x |= (1<<i)
            i += 1
        return x

            
