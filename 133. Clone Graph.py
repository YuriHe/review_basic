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
        if not node: return None

        # store cur_node: new_node (same v) memorization
        cloned_node = {}

        def clone(cur):
            # check if already clone node
            if cur in cloned_node:
                return cloned_node[cur]

            # set new Node with val
            new_node = Node(cur.val)
            cloned_node[cur] = new_node
            # set new Node with neighbors
            for n in cur.neighbors:
                # keep dfs, also add neighbor for new node
                new_node.neighbors.append(clone(n))
            # in the end return new node
            return new_node

        return clone(node)

        

