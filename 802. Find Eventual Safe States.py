class Solution:
    """
    Question: return safe nodes include no outgoing edges and node can lead to safe node
    Check if has cycle
    DFS
    """
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        res = []
        memo = {} # {node: T/F} represent safe 

        # check hascycle
        def dfs(node):
            if node in memo:
                return memo[node]
            # update memo
            # Assume cur node is not safe node, check adjcent nodes
            memo[node] = False
            for adj in graph[node]:
                if not dfs(adj):
                    return False
            # no safe through paths from this node
            memo[node] = True
            return memo[node]

        # iterate node
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res