# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: maximum path sum consider vertically and horizontally left+right+cur or max(left,right)+cur
    sending back to parent
    This is recursion, keep dfs until basic case and return back single data to parent
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxSum = float('-inf')

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            maxSum = max(maxSum, left+right+node.val)
            return max(left, right) + node.val

        dfs(root)

        return maxSum
        