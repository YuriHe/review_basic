class Solution:
    """
    Question: return list of large group which have duplicates substring >= 3times, return [start,end]
    ISSUE: check 'a', or last part
    """
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start = 0
        res = []
        for i in range(1, len(s), 1):
            if s[i] != s[i-1]:
                # stop prev group
                if i - 1 - start >= 2:
                    # it is large group
                    res.append([start, i-1])

                # update start
                start = i

            # check it after latest start update!
            if i == len(s)-1:
                # handle last section
                if len(s)-start >= 3:
                    res.append([start, len(s)-1])
        return res


        