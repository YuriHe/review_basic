class Solution:
    """
    Question: [[take, preq]] 
    eg.[[1,0],[2,0],[3,0],[4,1],[4,2],[5,4],[5,3]], total 5 class T-> True
    TOPIC: deque, find all pre of cur, and pop it out 
    Not use deque template(for tree)
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # store number of preq of cur course eg.[1,0],[1,2]
        preq = [0] * numCourses
        for p in prerequisites:
            preq[p[0]] += 1
        # store course without preq into queue's initial list
        q = collections.deque([])
        for i in range(len(preq)): # course range[0,...n-1]
            if preq[i] == 0: # cur course no preq
                q.append(i)
        level = 0
        # Only no preq's course can insert into queue
        while len(q) > 0:
            cur = q.popleft()
            # iterate prerequisites to insert course whose preq are cur
            for p in prerequisites:
                if p[1] == cur:
                    # find preq, mean p[0] this course can deduct one preq
                    preq[p[0]] -= 1
                    # (MUST CHECK AFTER -=1, otherwise TLE)if no preq of cur, ready to insert into q
                    if preq[p[0]] == 0:
                        q.append(p[0])
            level += 1
        return numCourses == level


