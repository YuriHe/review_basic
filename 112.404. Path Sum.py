# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    112. Path Sum
    Question: if there is root-leaf path can sum up to targetSum
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and targetSum - root.val == 0: 
            return True
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val) 


class Solution:
    """
    404. Sum of Left Leaves
    """
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node: return
            if node and node.left and not node.left.left and not node.left.right:
                # find left leaf
                res += node.left.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return res