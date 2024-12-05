class Solution:
    """
    Question: Find max weight probability of path
    Dijkstra's algorithm -> greedy, bfs -> maxheap + consider visited

    Time complexity:
    build graph: O(E), iterate edges and prob list 
    traverse graph: Dijkstra algorithm using max heap: heap operation: insertion+pop will take (logV) where V is the number of nodes
    and explore neighbors,traverse V's E edges, so time is O(ElogV)
    """
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # build graph
        adj = collections.defaultdict(dict)
        # for i in range(len(edges)):
        #     src, des = edges[i]
        #     # unidrect, so store both
        #     adj[src].append([des, succProb[i]])
        #     adj[des].append([src, succProb[i]])
        # 2way: use dict instead of list
        for (src, des), prob in zip(edges, succProb):
            adj[src][des] = prob
            adj[des][src] = prob

        # create maxheap
        heap = [(-1, start_node)]
        # mark if node is visited, use set since undirected
        visited = set()

        # traverse graph and keep max heap
        while heap:
            prob, v = heapq.heappop(heap)
            visited.add(v)

            # get result exit early since multiple will make prob smaller
            if v == end_node:
                return prob * -1
            # for nei, w in adj[v]:
            #     if nei not in visited:
            #         heapq.heappush(heap, (w * prob, nei))
            # 2way
            for child in adj[v]:
                if child not in visited:
                    heapq.heappush(heap, (adj[v][child] * prob, child))
        return 0


