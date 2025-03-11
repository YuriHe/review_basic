class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        SOLUTION1: valid N-ary tree, there are no cycled nodes 
        TIME SPACE O(V+E)
        """
        adj = collections.defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()

        def dfs(cur, prev):
            # base case
            if cur in visit: return False # found cycle
            visit.add(cur)

            for nei in adj[cur]:
                if prev == nei: # cur come from prev
                    continue
                # recursive in this certain path
                if not dfs(nei, cur):
                    return False
            # search all paths no cycle
            return True

        return dfs(0, -1) and len(visit) == n # no cycle & connected
