# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # root is smallest node see question
        self.minV, self.second = root.val, float('inf')
        def traverse(node):
            if not node: return
            traverse(node.left)
            if node.val > self.minV and node.val < self.second:
                # update second
                self.second = node.val
            traverse(node.right)
        traverse(root)
        return self.second if self.second != float('inf') else -1
