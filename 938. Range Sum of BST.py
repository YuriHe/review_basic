# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: sum up all val in [low, high]
    TOPIC: iterate BST 
    """
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = [0] * 1
        self.rec(root, low, high, res)
        return res[0]
    
    def rec(self, node, low, high, res):
        # base case
        if node is None:
            return 
        if node.val <= high and node.val >= low:
            res[0] += node.val
        # do recursion
        self.rec(node.left, low, high, res)
        self.rec(node.right, low, high, res)