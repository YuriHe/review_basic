class Solution:
    """
    Question:find left lastindex of cur string at i index meanwhile right
    dynamically remove char from string? yes
    find pattern 
    eg.
    1.a
    2.aa
    3.a__a__a->a 1
    4.a__a_a_a->aa 2
    5.a_a_aa_a->a 1
    6.a_aaaa_a->aa 2
    -> find pattern: if freq(char) is odd-> len(char)=1, else len(char)=2
    """
    def minimumLength(self, s: str) -> int:
        # len > 2 otherwise nothing to delete
        if len(s) <= 2: return len(s)
        ctn = Counter(s)
        res = 0
        for char, count in ctn.items():
            if count % 2 == 0:
                res += 2
            else:
                res += 1
        return res

                