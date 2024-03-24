class Solution:
    """
    Question: find largest odd number(substring)in string 
    TOPIC: MATH, if last digit is odd, that num is odd
    ISSUE: NOT THINK there is not substring in the middle, JUST check last of digit start last to 0
    """
    def largestOddNumber(self, num: str) -> str:
        i = len(num)-1
        while i >= 0:
            # convert cur str to int(not Whole num)
            n = int(num[i])
            if n % 2 != 0: # it is odd return it 
                return num[0:i+1]
            i -= 1
        return ""


        