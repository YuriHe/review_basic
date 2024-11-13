class Solution:
    """
    Question: Kill next closet opponent,who left will win
    Create two queues, store R D's index. Who index smaller will win this round
    This round-base, who win will go to back of line index+len
    """
    def predictPartyVictory(self, senate: str) -> str:
        q1 = deque([])
        q2 = deque([])

        for i, c in enumerate(senate):
            if c == "R":
                q1.append(i)
            else:
                q2.append(i)

        while len(q1) > 0 and len(q2) > 0:
            first1 = q1.popleft()
            first2 = q2.popleft()
            if first1 < first2:
                # first1 win
                q1.append(first1+len(senate))
            else:
                # first2 win
                q2.append(first2+len(senate))
        
        if len(q1) > 0:
            return "Radiant"
        else:
            return "Dire"
