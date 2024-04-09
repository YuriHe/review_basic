class Solution:
    """
    Question: count total time for k index, if ticket=0 then leave queue. so queue size is changing 
    and val at k index is changing
    TOPIC: QUEUE
    """
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        time = 0
        # store index to queue
        for i in range(len(tickets)):
            q.append(i)
        # line in queue until k done     
        while len(q) > 0:
            front = q.popleft()
            # count 1 time
            time += 1
            # bought one ticket
            tickets[front] -= 1
            # person at k and bought all tickets already, no left tickets
            if front == k and tickets[front] == 0:
                return time
            # if still have tickets go to back, next queue, otherwise leave queue
            if tickets[front] != 0:
                q.append(front)
        return time
            

