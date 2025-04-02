class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        SOLUTION1: topological sort (Kahn's algorithm BFS)
        directed,acyclic graph 
        """
        # Step1: build graph and in-degree map
        graph, indegree = self.build_graph(words)

        # Step2: perform topological sort on graph
        res = self.topo_sort(graph, indegree)

        if len(res) != len(indegree):
            return ""
        return "".join(res)
    
    def build_graph(self, words):
        """
        Build the graph and in-degree map from the given words.
        Each character will be a node, and edges represent the precedence
        """
        adj = collections.defaultdict(set) # a: set(b,c)
        indegree = collections.defaultdict(int) # track dependencies a->b, b+1
        # initialize indegree for all chars
        for word in words:
            for c in word:
                indegree[c] = 0
        # build graph by comparing adj words
        for i in range(1, len(words)):
            first = words[i-1] # a ->
            second = words[i] # b

            # find first char different between two words
            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    if second[j] not in adj[first[j]]:
                        adj[first[j]].add(second[j])
                        indegree[second[j]] += 1
                    break # first first diff will out of searching
            
            if first.startswith(second) and len(first) > len(second): # abc, ab 
                return {}, {}

        return adj, indegree

    def topo_sort(self, adj, indegree):
        """
        Perform topological sorting on the graph using Kahn's algorithm.
        """
        q = deque([])
        res = []

        for c, v in indegree.items():
            if v == 0:
                q.append(c) # push no indegree character(first char in alien dict)
        
        while q:
            node = q.popleft()
            res.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res
