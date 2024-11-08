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


class Solution:
    """
    Question: if can finish all courses
    premap: [cur]: [preqs]
    visited.set avoid loop
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create premap to check cur, preq
        premap = {i: [] for i in range(numCourses)}
        for pre in prerequisites:
            premap[pre[0]].append(pre[1])
        # visitset to check cur=preq loop scene along with dfs 
        visit = set()

        def dfs(cur) -> bool:
            # base case
            if cur in visit:
                return False
            if premap[cur] == []: # no pre
                return True

            visit.add(cur)
            for preq in premap[cur]:
                if not dfs(preq):
                    return False
            # reset for tracking cur's all preq
            visit.remove(cur)
            premap[cur] = []
            # finally return
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
