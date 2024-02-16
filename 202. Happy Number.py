"""
    Question: Understand happy number
    TODO: put the sum of squares of each digit into loop, 
    until sum ==1 will jump out of loop or loop endless which not =1
    TOPIC: use set, if seen
"""
def isHappy(self, n: int) -> bool:
    seen = set()
    while n != 1:
        # replace n
        n = self.isSum(n)
        if n in seen:
            return False
        seen.add(n)
    return True

def isSum(self, n)-> int:
    total = 0
    while n > 0:
        total += (n%10) ** 2
        n //= 10
    return total
        