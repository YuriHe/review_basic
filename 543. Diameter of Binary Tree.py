# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: find longest path between two nodes, maynot across the root
    DFS
    res is getting largest diameter
    dfs return is getting cur's maximum depth
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 0

        def dfs(node) -> int:
            nonlocal res
            if not node:
                 return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left+right)

            # cur node return max between left, right
            return max(left, right) + 1

        dfs(root)
        return res