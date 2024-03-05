"""
    Question: Handle digits
    Topic: math, sort
"""
def sequentialDigits(self, low: int, high: int) -> List[int]:
    res = []
    # outer loop increase first digit in each num [1,9]
    for i in range(1, 10):
        # intial num and incre, num will store into list, incre create new digit 
        num = incre = i 
        # if num in[low, high] store into res, otherwise keep incre++
        while num <= high and incre < 10:
            if num >= low:
                res.append(num)
            incre += 1
            num = num*10+incre # 12. 123. 1234. 
    return sorted(res)