import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: BT BFS(breadth first search), search level by level
    TOPIC: BFS=QUEUE
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        q = collections.deque([root])
        res = []
        while len(q) > 0:
            inner = []
            # define size first, otherwise size will change
            size = len(q)
            while size > 0:
                first = q.popleft()
                inner.append(first.val)
                if first.left: 
                    q.append(first.left)
                if first.right:
                    q.append(first.right)
                
                size -= 1
            # done one level
            res.append(inner)

        return res

                
        return res