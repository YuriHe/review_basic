# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: turn bt to right-leaning linkedlist
    start root -> check left node -> 
    """
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        connect from back to front
        """
        if not root: return None
        cur = root

        while cur:
            # check if cur have left, adjust pointer to left subtree
            prev = cur.left
            if prev:
                # find rightmost in left subtree
                while prev.right:
                    prev = prev.right
                # insert entire left subtree to the cur right subtree
                prev.right = cur.right
                # make left subtree to the right
                cur.right = cur.left
                cur.left = None

            cur = cur.right # left subtree root




        