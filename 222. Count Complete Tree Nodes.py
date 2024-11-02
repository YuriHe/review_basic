# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: iterate tree and count nodes
    Return is returning cur node situation
    """
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.countNodes(root.left)
        r = self.countNodes(root.right)
        # add 1 for cur node
        return l + r + 1


        