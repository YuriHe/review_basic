"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        """
        SOLUTION1: BFS -> find maximum depth
        """
        # find maximum depth
        self.level=0
        if not root:
            return self.level
        q = deque([root])
        while q:
            size = len(q)
            while size > 0:
                first = q.popleft()
                if first.children:
                    for child in first.children:
                        q.append(child)
                size -= 1
            self.level += 1
        return self.level