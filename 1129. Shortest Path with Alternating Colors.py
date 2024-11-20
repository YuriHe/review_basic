class Solution:
    """
    Direct graph
    BFS find shortest path + see if alternating path is from 0 to any node, otherwise return -1
    STEP:
    1.create red, blue dict store {src: [dest]}
    2.define q: [node, length, prev_edge_color]
    3.define visited: (node, pre_edge_color)
    4.enter q, update answer[node] which is shortest 
    5.if 'RED' cur edge, go to all 'BLUE' neighbors; same as 'BLUE'. work on simultaneously
    """
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # define red blue edges 
        red = defaultdict(list)
        blue = defaultdict(list)
        # fill out edges
        for src, dest in redEdges:
            red[src].append(dest)
        for src, dest in blueEdges:
            blue[src].append(dest)

        # define answer list
        res = [-1] * n
        q = deque()
        q.append([0, 0, None]) # [Node, length, prev_edge_color] start from 0 Node
        visit = set()
        visit.add((0, None)) # (Node, prev_edge_color)

        while q:
            cur, length, edge = q.popleft()
            if res[cur] == -1:
                # return right now to get shortest path
                res[cur] = length
            
            if edge != "RED":
                # check red edges neighbors from cur node
                for nei in red[cur]:
                    # go to nei, need to check if nei is visited or not
                    if (nei, "RED") not in visit:
                        visit.add((nei, "RED"))
                        q.append([nei, length+1, "RED"])
            
            # search simutaneously with red edge
            if edge != "BLUE":
                for nei in blue[cur]:
                    if (nei, "BLUE") not in visit:
                        visit.add((nei, "BLUE"))
                        q.append([nei, length+1, "BLUE"])
        return res


    