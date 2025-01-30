class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        1.Solution:Union find handle undirected graph
        Question:Remove extra edge(last) to make graph is tree(no cycle), current have cycle, Cycle detect
        Idea:Iterate edges, if cannot union,return right away; find logic when if same node(same parent), if yes, return
        cannot union(since found cycle)
        Time: O(V+E)
        Space: parent rank array
        """
        n = len(edges)
        # vertice start 1, so size+1
        parent = [i for i in range(n+1)]
        rank = [1 for _ in range(n+1)]

        def find(n):# path compression, flatten tree from cur to root
            cur = n
            while cur != parent[cur]:
                cur = parent[cur]
                parent[cur] = parent[parent[cur]]
            return cur

        def union(n1, n2):
            r1, r2 = find(n1), find(n2)
            if r1 == r2: # point to same node, cycle detected
                return False
            if rank[r1] > rank[r2]:
                parent[r2] = r1
                rank[r1] += rank[r2]
            else:
                parent[r1] = r2
                rank[r2] += rank[r1]
            return True

        # iterate edge 2d
        for v1, v2 in edges:
            if not union(v1, v2):
                return [v1, v2]
        return []