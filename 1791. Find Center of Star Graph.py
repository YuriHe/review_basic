class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        SOLUTION1: undirected graph
        STEP: create indegree dict, if val=len of edges mean this vertex is center
        """
        indegree = {}
        for v1, v2 in edges:
            indegree[v1] = indegree.get(v1, 0) + 1
            indegree[v2] = indegree.get(v2, 0) + 1
        for k, v in indegree.items():
            if v == len(edges):
                return k
        return -1


