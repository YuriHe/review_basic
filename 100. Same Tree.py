# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Quesstion: check if two binary tree are same
    Topic: iterate tree 
    T: O(n)
    S:O(1)
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (not p and q): return False
        # another way
        # if p is None and q is not None: return False
        # if q is None and p is not None: return False

        # this must have before check .val
        if q is None and q is None: return True
        elif p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)