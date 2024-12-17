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
        max_sum = float('-inf')

        def helper(node):
            nonlocal max_sum
            if not node:
                return 0
            # recursively traverse left subtree from top to bottom 
            left = max(0, helper(node.left))
            right = max(0, helper(node.right))
            # update max sum from horizontal
            max_sum = max(max_sum, left+right+node.val)
            # from basic case sending back to already traversed node: vertically
            return max(left,right) + node.val

        helper(root)
        return max_sum
        
        