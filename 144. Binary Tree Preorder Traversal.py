# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    144. Binary Tree Preorder Traversal
    1way: recursion
    2way:
    Use stack
    push root, right, then left
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 1. Recursion Way
        res = []

        def rec(node):
            # base case
            if not node: return 
            res.append(node.val)
            rec(node.left)
            rec(node.right)

        rec(root)
        return res

        # 2. Iterative Way
        if not root: return []
        stack = []
        res = []
        # push root first, make sure can process stack
        stack.append(root)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res