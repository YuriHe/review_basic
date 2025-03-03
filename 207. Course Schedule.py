class Solution:
    """
    Question: Check if can finish all courses, [[cur, preq]]
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        SOLUTION1: BFS
        STEP:
        1.create indegree list for counting number of preq at i(label of course)
        2.create queue store label of courses
        3.hashmap (preq: [cur1, cur2])
        4.finished == n
        """
        indegree = [0] * numCourses
        courses = collections.defaultdict(list)
        q = deque([])
        finished = 0

        for cur, preq in prerequisites:
            indegree[cur] += 1
            courses[preq].append(cur)

        for i, v in enumerate(indegree):
            if v == 0: # no preq, take right away
                q.append(i)
        
        while q:
            finished += 1
            cur = q.popleft()
            # search dic see if have other course' preq is cur
            if cur in courses:
                for v in courses[cur]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        # push into q
                        q.append(v)
        return finished == numCourses

                
