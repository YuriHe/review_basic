# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        better pos is the one have parent and child
        2 mean cur no cover, wait parent cover;
        1 mean cur no need cover, either child cover;
        0 mean cur need cover, either child no cover
    """
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # number of camera
        res = 0
        # step iterate tree
        def rec(node):
            nonlocal res
            if not node: 
                return 2
            # from top to down
            l= rec(node.left)
            r= rec(node.right)
            # handle basic and down to top
            if l == 0 or r == 0:
                # child no covered
                res+= 1
                # add camera for current node
                return 1 
            elif l == 1 or r == 1:
                # either child is covered
                # current node covered as well 
                return 2
            elif l == 2 and r == 2:
                # eg.l==2 and r==2
                # leaf are not covered, we wait our parent cover us
                # current node nothing do
                return 0
        # handle root explicitly
        if rec(root) == 0:
            res += 1
        return res