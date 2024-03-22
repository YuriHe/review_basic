# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: find minimum depth of bt
    ISSUE: NOT: 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    TOPIC: queue, if find it is leaf return right away
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root: return 0
        q = collections.deque([root])
        level = 1
        while len(q) > 0:
            size = len(q)
            while size > 0:
                first = q.popleft()
                if not first.left and not first.right: # it is leaf
                    return level 
                if first.left:
                    q.append(first.left)
                if first.right:
                    q.append(first.right)
                size -= 1
            level += 1
        return level
