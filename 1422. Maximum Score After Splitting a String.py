class Solution:
    """
Question: return maximum score when keep spliting two zero/one strings
Step: right1 count first, left0 +=1 right1 -=1, corner case"00"->1, skip last v
    """
    def maxScore(self, s: str) -> int:
        # SOLUTION1
        if len(s) < 2: return 0 # no score
        res = 0
        left, right = 0, 1
        while right < len(s):
            score = s[left:right].count("0") + s[right:].count("1")
            res = max(score, res)
            right += 1
        return res
        # SOLUTION2: prepare zero one count
        right1 = s.count("1")
        res, left0 = 0,0

        for i in range(len(s)-1):
            if s[i] == "0":
                left0+=1
            else:
                right1-=1
            # current split
            score = left0+right1
            res = max(res, score)
        return res

                

        