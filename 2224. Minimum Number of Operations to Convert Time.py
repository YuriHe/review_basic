class Solution:
    """
    2224. Minimum Number of Operations to Convert Time
    Question: handle time on clock
    Use greedy, math, string
    edge case: 23:59 -> 00:00 -> expected 1 
    """
    def convertTime(self, current: str, correct: str) -> int:
        res = 0
        tries = [60, 15, 5, 1]
        i = 0
        
        # calculate difference, handle wraparound
        curMin = int(current[:2]) * 60 + int(current[3:])
        corMin = int(correct[:2]) * 60 + int(correct[3:])
        if corMin < curMin:
            corMin += 24 * 60
        diff = corMin- curMin

        # greedy way
        while diff > 0:
            if diff >= tries[i]:
                # add operation times
                res += diff // tries[i]
                # reduce diff
                diff %= tries[i]
            else:
                i += 1
        return res


            