# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """106. Construct Binary Tree from Inorder and Postorder Traversal
    Question: 
    inorder array, [:root] is left, [root+1:] is right subtree, iterate/recursion
    build a tree
    """
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0: return None
        # last one in postorder is root of cur subtree
        # create node of tree
        root = TreeNode(postorder.pop())
        mid = inorder.index(root.val)
        # build right tree first 
        root.right = self.buildTree(inorder[mid+1:], postorder)
        root.left = self.buildTree(inorder[:mid], postorder)
        return root
