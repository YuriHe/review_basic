# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: if subroot tree is desecendant of parent tree
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        SOLUTION1: iterate tree check if there is any subtree is same tree as subroot tree
        TIME: (M*N) SPACE(M+N) M is node number of root, N is node number of subroot
        """
        # if parent is empty tree, cannot have subtree
        if not root: return False
        # if subtree is empty tree, it can be subtree of any tree
        if not subRoot: return True
        if self.isSameTree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, t1, t2):
        if not t1 and not t2:  return True
        if (not t1 and t2) or (not t2 and t1):return False
        if t1.val != t2.val:return False
        return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)
