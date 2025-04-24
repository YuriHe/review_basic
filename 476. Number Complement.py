class Solution:
    def findComplement(self, num: int) -> int:
        """
        SOLUTION1: conversion
        """
        # convert decimal number to binary string
        s = bin(num)[2:]
        # flip 1 to 0
        flip_bin_s = ''.join('0' if v == '1' else '1' for v in s)
        # convert binary string to decimal num
        return int(flip_bin_s, 2)

        """
        SOLUTION2: Bit
        """
        bit_len = num.bit_length() # 5:101-> 3
        mask = (1<< bit_len) - 1 # (return decimal) shift 1 left by bit_len:1000-1=0111(binary)=8(decimal)-1=7
        return num ^ mask #101(5) ^0111(7)=010(2)