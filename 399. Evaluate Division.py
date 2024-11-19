class Solution:
    """
    Question: convert this equations to diected weight graph
    BFS
    """
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build graph store (src: [[des1, value], [des2, value]])
        adj = defaultdict(list)
        for i, v in enumerate(equations):
            # a: [b, v], b:[a, 1/v]
            a,b = v
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])
        
        # use bfs to get one query'result
        def bfs(src, target):
            q = deque()
            q.append([src, 1])
            visited = set()
            visited.add(src)

            if src not in adj or target not in adj:
                return -1
            
            while q:
                n, w = q.popleft()
                if n == target:
                    return w # that is result
                for ne, weight in adj[n]:
                    if ne not in visited:
                        q.append([ne, w * weight])
                        visited.add(ne)
            return -1
        return [bfs(q1, q2) for q1, q2 in queries]


