"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        res = []

# BFS 
if not root: return []
q = deque([root])
while q:
    size = len(q)
    inner = []
    for _ in range(size):
        first = q.popleft()
        inner.append(first.val)
        # push children into queue
        for c in first.children:
            q.append(c)
    # finish one layer
    res.append(inner)
return res

