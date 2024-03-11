# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question:  A binary tree is balanced if the heights of 
    its left and right subtrees differ by at most 1 for every node in the tree.
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        # compare left subtree and right subtree max height
        if abs(self.get_max_height(root.left) - self.get_max_height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_max_height(self, node) -> int:
        if node is None: return 0
        return 1 + max(self.get_max_height(node.left), self.get_max_height(node.right))