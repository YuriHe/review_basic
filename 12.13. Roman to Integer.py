class Solution:
    """
    12. Integer to Roman
    Convert int to Roman
    Use greedy, math  while num > 0,deduct num
    """
    def intToRoman(self, num: int) -> str:
        res = ""
        # handle corner case
        if num < 1 or num > 3999:
            return res
        # iterate two array at the same time instead of handle multiple combination
        weight = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        token = ['M','CM','D','CD','C', 'XC', 'L','XL','X','IX','V','IV', 'I']
        i = 0
        while num > 0:
            if num >= weight[i]:
                res += token[i]
                num -= weight[i]
            else:
                # use next token 
                i += 1
        return res


class Solution:
    """
    13. Roman to Integer
    Question: convert roman to integer and sum them up in str
    Find math pattern
    """
    def romanToInt(self, s: str) -> int:
        # use map store roman mapping to int
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        for i in range(len(s)):
            if i < len(s) - 1 and dic[s[i]] < dic[s[i+1]]:
                res -= dic[s[i]]
            else:
                res += dic[s[i]]
        return res


        