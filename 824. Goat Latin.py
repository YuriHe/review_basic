"""
    Question: Understand rules 
    Modify value
"""
def toGoatLatin(self, sentence: str) -> str:
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        ls = sentence.split(" ")
        res = []
        for i, word in enumerate(ls):
            tmp = ""
            if word[0] in vowels:
                tmp += word + "ma" + (i+1)*"a"
            else:
                tmp += word[1:] + word[0] + "ma" + (i+1) * "a"
            res.append(tmp)
        return " ".join(res)
