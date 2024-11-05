# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def rec(node, inner):
            if not node:
                return
            if not node.left and not node.right: # it is leaf
                inner += str(node.val)
                res.append(inner)
                return
            # recursion
            inner = inner + str(node.val) + "->"
            rec(node.left, inner)
            rec(node.right, inner)

        rec(root, "")
        return res