# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    QUESTION: return re-constructed BST
    """
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode()
        cur = dummy

        def inorder(node):
            nonlocal cur
            if not node:
                return 
            
            inorder(node.left)
            # create new treenode
            cur.right = TreeNode(node.val)
            # moving pointer
            cur = cur.right
            inorder(node.right)

        # traverse original tree
        inorder(root)
        # return new tree
        return dummy.right