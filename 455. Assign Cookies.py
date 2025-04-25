class Solution:
    """
    QUESTION: minimal cookie waste and maximal satisfaction
    SAME as 2410. Maximum Matching of Players With Trainers
    """
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        SOLUTION1: greedy, two pointer, sort
        """
        # sort greedy factor and cookie size
        g.sort()
        s.sort()
        # two pointer, track children, cookie
        # for each child, assign smallest cookie that satisfies them
        # if satisfied, move to next children.always move to next cookie
        i, j, ctn = 0,0,0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                # satisfied for cur children i
                ctn += 1
                # move to next child
                i += 1
            # no matter satified cur child or not, move to next cookie
            j += 1
        return ctn
