# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.flag = root.val
        def traverse(node):
            if not node:return True
            if node.val != self.flag:
                return False
            return traverse(node.left) and traverse(node.right)
        return traverse(root)