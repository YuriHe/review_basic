class Solution:
    """
    Question: index queueing to buy ticket until ticket = 0
    How to find index -> create q storing index
    if found ticket = 0, remove from q
    """
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque([])
        res = 0
        for i in range(len(tickets)):
            q.append(i)
        
        while len(q) > 0:
            first = q.popleft()
            tickets[first] -= 1
            res += 1
            if tickets[k] == 0:
                return res
            if tickets[first] > 0:
                q.append(first)
            
        return res

