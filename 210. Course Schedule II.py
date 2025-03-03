class Solution:
    """
    Question:return list of ordering to finish courses
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        SOLUTION1: BFS
        STEP:
        1.create indegree list for counting number of preq at i(label of course)
        2.create queue store label of courses
        3.hashmap (preq: [cur1, cur2])
        4.finished == n, if not return empty list
        """
        indegree = [0] * numCourses
        courses = collections.defaultdict(list)
        q = deque([])
        finished = 0
        res = []

        for cur, preq in prerequisites:
            indegree[cur] += 1
            courses[preq].append(cur)

        for i, v in enumerate(indegree):
            if v == 0: # no preq, take right away
                q.append(i)
        
        while q:
            finished += 1
            cur = q.popleft()
            res.append(cur)
            # search dic see if have other course' preq is cur
            if cur in courses:
                for v in courses[cur]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        # push into q
                        q.append(v)
        return res if finished == numCourses else []
