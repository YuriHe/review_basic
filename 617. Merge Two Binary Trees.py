# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    QUESTION: merge two binary tree to one tree; if not exist, create new node; if already exist, then add value
    """
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        SOLUTION1: recursion, merge into first tree
        """
    if not root1: return root2
    if not root2: return root1
    root1.val += root2.val
    root1.left = self.mergeTrees(root1.left, root2.left)
    root1.right = self.mergeTrees(root1.right, root2.right)
    return root1