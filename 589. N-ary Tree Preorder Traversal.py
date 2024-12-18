"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # 1.Iterative
        if not root: return []
        res = []
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            for i in range(len(cur.children)-1, -1, -1):
                stack.append(cur.children[i])
        return res