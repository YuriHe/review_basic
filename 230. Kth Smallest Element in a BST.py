# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: find kth smallest element in BST

    SOLUTION1: inorder recusion
    Iterate bst by inorder and generate list
    recursion is slow 
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ls = []
        def inorder(node) -> None:
            # base case
            if not node:
                return
            # iterate left
            inorder(node.left)
            ls.append(node.val)
            # iterate right
            inorder(node.right)

        inorder(root)

        return ls[k-1]

"""
    SOLUTION2: Iterative inorder traversal by stack
"""
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # create stack list store all nodes
    stack = []
    # define cur for traverse bst 
    cur = root

    # looping stack or nodes if exist
    while cur or stack:
        # push all left nodes of cur if exist
        while cur:
            stack.append(cur)
            cur = cur.left
        
        # pop first smallest, reassign cur
        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val
        
        # iterate right
        cur = cur.right
