class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 0 
        res = [0] * len(digits)
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return digits # return right away only modify(+1) last index v
            else:
                digits[i] = 0
        # reach here mean need to add leading 1
        res.insert(0, 1)
        return res 
        


        