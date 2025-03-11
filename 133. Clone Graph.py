"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        SOLUTION1: BFS
        TIME: O(V+E)
        SPACE: O(V)
        """
        if not node: return None

        q = deque([node])
        # mapping old to newnode
        clone = {node: Node(val=node.val, neighbors=[])}

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in clone:
                    # create map
                    clone[nei] = Node(val=nei.val,  neighbors=[])
                    # q only store univisted node
                    q.append(nei)
                clone[nei].neighbors.append(clone[cur])
        return clone[node]


        

