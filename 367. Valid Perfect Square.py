class Solution:
    """
    QUESTION: verify if number is square of one integer
    """
    def isPerfectSquare(self, num: int) -> bool:
        """ 
        SOLUTION1: iterate ending to half of nums + binary search
        TIME: log(n/2)
        """
        if num <= 1:
            return True
        low = 1
        hi = num // 2
        while low <= hi:
            mid = (low + hi)//2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                hi = mid - 1
            else:
                low = mid + 1

        return False