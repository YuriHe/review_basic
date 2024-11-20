class Solution:
    """
    Question: get total time to inform all employees
    directed graph, tree, from manager to employee, no cycle no visit
    manager[i] is direct manager of i.
    inform[i] is time from direct manager. will inform simutanously
    layer by layer -> BFS, count maxium of total time
    STEP:
    1.from headID know who is CEO from node(0...n)
    2.define q, [Node, accumulatingT]
    3.res variable keep update to get max when simutanous process
    """
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # build graph/tree starting from manager
        adj = defaultdict(list)
        for i, lead in enumerate(manager):
            adj[lead].append(i)
        
        # define q
        q = deque()
        q.append([headID, informTime[headID]]) # node, time
        res = 0

        while q:
            cur, time = q.popleft()
            res = max(res, time)

            for nei in adj[cur]:
                # tracking employees of nei
                q.append([nei, time + informTime[nei]])
        
        return res


