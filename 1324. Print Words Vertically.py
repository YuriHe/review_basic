class Solution:
    """
    Question: Handle string vertically
    eg. "TO BE AAAA" -> [TBA, OEA,_ _A, _ _A], can left trailing, not right trailing spaces
    """
    def printVertically(self, s: str) -> List[str]:
        ls = s.split(" ")
        # find word with max length in list
        max_len = max(len(w) for w in ls)
        # make all word at same length(max_len), if short, use * to fill
        # [TO**, BE**, AAAA]
        for i in range(len(ls)):
            ls[i] += (max_len-len(ls[i])) * ("*")
        res = []
        # vertically print word in the list
        for i in range(max_len): # now all word in ls are same length(max_len)
            temp = ""
            for j in range(len(ls)):
                temp += ls[j][i]
            res.append(temp)
        # replace all * to " " and remove left trailing spaces
        for i in range(len(res)):
            res[i] = res[i].replace("*", " ").rstrip()
        return res

        





        