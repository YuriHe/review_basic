# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: count good node in bt from root to X (it is greatest)
    DFS keep update res, maxV is update for specific path, cannot affect on other path/globally
    [2,null,4,10,8,null,null,4] -> 4, not 3
    """
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0

        def rec(node, maxV):
            nonlocal res
            if not node:
                return
            # check if good node
            if node.val >= maxV:
                maxV = node.val
                res += 1
            rec(node.left, maxV)
            rec(node.right, maxV)
            
        rec(root, float('-inf'))
        return res