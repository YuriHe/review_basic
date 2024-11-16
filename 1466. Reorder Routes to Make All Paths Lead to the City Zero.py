class Solution:
    """
    Question: count changing path toward to 0, directed graph
    DFS 
    start from 0, check all neighbors of 0, direction use (neighbor, curcity(close 0)) exit in connections
    1.visitedset store city
    2.edges set store connection as set instead of list 
    """
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0
        visited = set()
        visited.add(0)
        neighbors = defaultdict(list)
        edges = {(a,b) for a,b in connections} # as set avoid duplicates

        # fill out neighbor (include ingoing and outgoing)
        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(cur):
            nonlocal res

            for city in neighbors[cur]: 
                if city in visited:
                    continue
                visited.add(city)
                # travel city to cur(near 0)
                if (city, cur) not in edges:
                    res +=1
                
                # no matter change edges or not, still dfs, check city as cur's edges
                dfs(city)

        dfs(0)
        return res
