# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Question: find one node is lowest command ancestor of st start from [p,q]nodes, allow ancestor also descendant
    p and q node are both existed
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if root == p or root == q: return root # cur is descendant also ancestor from top to down
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: # both are not None, the they share same ancestor
            return root
        else:
            return left or right # find one of both is descendant also ancestor

        