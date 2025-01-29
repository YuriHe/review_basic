class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        1.Solution: Union find(Disjoin Set)
        Idea:Iterate 2D, if connected, try to merge
        """
        n = len(isConnected)
        # define parent, default itself
        parent = [i for i in range(n)]
        # define rank, default itself count 1
        rank = [1 for _ in range(n)]
        def find(n1):
            # iterate from now to root parent
            cur = n1
            while cur != parent[cur]:# until move to root parent or reach itself
                # move pointer to parent
                cur = parent[cur]
                parent[cur] = parent[parent[cur]]
            return cur
        def union(n1, n2):
            # find root parent of n1, n2
            r1, r2 = find(n1), find(n2)
            # same node
            if r1==r2:
                return 0
            # merge smaller group into larger group
            if rank[r1] > rank[r2]:
                # point r2's parent to r1
                parent[r2] = r1
                # r1 have new member,merge new member's rank
                rank[r1] += rank[r2]
            else:
                parent[r1] = r2
                rank[r2] += rank[r1]
            return 1
        # iterate 2d; At most goup is N nodes, each of them alone
        group = n 
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    group -= union(i, j)
        return group

    """
        2.Solution: DFS (Better)
        Idea:iterate all city, start from univist do dfs, marked all connected cities visited, stop until 
        all cities are visited
        Time:O(n^2): iterate all cities, inside dfs, iterate all neighbor of cur city 
        Space:O(n): visited array
    """
    # N vertices, at most N edges(cycle), if tree is N-1 edge
    n = len(isConnected)
    visited = [False] * n
    group = 0

    def dfs(n):
        # base case
        if visited[n]:
            return
        visited[n] = True
        for nei, conn in enumerate(isConnected[n]):
            if conn == 1 and not visited[nei]:
                dfs(nei)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            group += 1
    return group