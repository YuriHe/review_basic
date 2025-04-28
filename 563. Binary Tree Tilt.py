# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    QUESTION: return sum of all node's absolute difference between node's left and right subtree
    """
    def findTilt(self, root: Optional[TreeNode]) -> int:
        # as gobal value, keep adding to this total
        total = 0

        def rec(node):
            nonlocal total
            if not node: # this is leaf no child
                return 0
            # traverse recursively until reach leaf
            left_sum = rec(node.left)
            right_sum = rec(node.right)
            # now reach base case, update total
            total+=abs(left_sum - right_sum)
            # pass left/rightsum + cur to cur's parent's branch's subsum
            return left_sum + right_sum + node.val
        # call helper, no need return
        rec(root)
        # return global value
        return total
            