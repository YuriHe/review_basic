# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    1372. Longest ZigZag Path in a Binary Tree
    Question: dfs, single node's length=0
    can get part of path, not just root to left
    """
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # SOLUTION1: duplicate recursion
        if not root: 
            return 0
        res = 0

        def dfs(node, toright, step):
            nonlocal res
            if not node:
                return
            # update res
            res = max(res, step)
            if toright:
                dfs(node.left, False, step+1) #already in right, need to move to left
                dfs(node.right, True, 1) # already in right, restart to right with 1
            else:
                dfs(node.left, False, 1) # already in left, restart to left with 1
                dfs(node.right, True, step+1) # already in left, move to right

        # handle two direction
        dfs(root, True, 0)
        dfs(root, False, 0)
        return res

        # SOLUTION2: optimize
        if not root:
            return 0
        res = 0

        def dfs(node, ll, rl):
            nonlocal res
            if not node:
                return
            # update res
            res = max(res, ll, rl)
            # traverse left tree, from right, accumulate zigzag length, reset right length
            dfs(node.left,rl+1, 0)
            # traverse right tree, from left, accumlate zigzag length, reset left
            dfs(node.right,0,ll+1)
        
        # handle leftL, and rightL
        dfs(root, 0, 0)
        return res
