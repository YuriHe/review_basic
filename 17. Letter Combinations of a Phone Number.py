class Solution:
    """
    Question: Combination - backtracking find k slot
    4 ^n(digit length)
    """
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or len(digits) == 0: return []
        # define digit-letters mapping {2:"abc"}
        phone = { 
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        res = []

        def rec(idx, inner):
            if idx == len(digits): # done one combination
                res.append("".join(inner))
                return 
            for c in phone[digits[idx]]:
                inner.append(c)
                rec(idx+1, inner)
                inner.pop()
        rec(0, [])
        return res
