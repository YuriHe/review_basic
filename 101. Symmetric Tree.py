# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.rec(root, root)

    def rec(self, l, r):
        # base case
        if (l and not r) or (r and not l): return False
        if not l and not r: return True
        if l.val != r.val: return False
        return self.rec(l.left, r.right) and self.rec(l.right, r.left)

# SOLUTION2 Closure
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return False

        def rec(l, r) -> bool:
            if (l and not r) or (r and not l): return False
            if not l and not r: return True
            if l.val != r.val: return False
            return rec(l.left, r.right) and rec(l.right, r.left)
        

        return rec(root.left, root.right)