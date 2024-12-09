# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    530. Minimum Absolute Difference in BST
    783. Minimum Distance Between BST Nodes
    Question: minimum absolute difference in BST -> asking minimum difference between two nodes which near each other
    BFS inorder will give sorted order
    Iterate tree by using inorder, after left children recursion, handle parent, update ancestor(prev), then right children recursion
    Tracking diff = |lastest ancestor - each children|, udpate diff
    """
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        diff = float('inf')
        prev = None

        def inorder(node):
            nonlocal diff, prev # maake diff and prev accessible and mutable
            if not node: return 
            inorder(node.left)
            
            if prev and node:
                diff = min(diff, abs(prev.val - node.val))
            prev = node

            inorder(node.right)
            
        inorder(root)
        return diff


        