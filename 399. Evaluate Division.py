class Solution:
    """
    Question: convert this equations to diected weight graph
    BFS
    T: 
    build graph: O(n), n is number of equations or values
    bfs: each query will traverse every node and edge O(V+E)
    total is m * O(E+V) + O(n), m is number of query
    """
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # graph , bfs, deque, directed weight, visit
        # create graph
        adj = defaultdict(list) # src: [des, val]
        for i, v in enumerate(equations):
            src, des = v
            adj[src].append([des, values[i]])
            adj[des].append([src, 1/values[i]])

        # bfs and lookup adj dic, find des child (cross many relatives)
        def bfs(src, des):
            # handle undefine
            if src not in adj or des not in adj:
                return -1

            # create queue
            q = deque([])
            q.append((src, 1))
            visit = set()
            visit.add(src)

            while q:
                cur, val = q.popleft()
                # find des child, exit early
                if cur == des:
                    return val
                
                for nei, w in adj[cur]:
                    if nei not in visit:
                        q.append((nei, val*w))
                        visit.add(nei)
            
            return -1

        # iterate query from graph and do bfs
        return [bfs(src, des) for src, des in queries]
