"""
    Question: Understand rules 
    Modify value
    """
    def toGoatLatin(self, sentence: str) -> str:
        ls = sentence.split(" ")
        a = 1
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        for i in range(len(ls)):
            c = ls [i]
            first = c[0]
            if len(c) > 1:
                for j in range(len(c)):
                    if j == 0 and c[j] not in vowels:
                        # if c is single char no need to delete+append
                        c = c[1:] 
                        c += first
            c += "ma" + "a" * a
            ls[i] = c
            a += 1
        return " ".join(ls)

