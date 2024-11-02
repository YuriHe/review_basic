# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    105. Construct Binary Tree from Preorder and Inorder Traversal
    Question: 
    inorder array, [:root] is left, [root+1:] is right subtree, iterate/recursion
    build a tree
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0: 
            return None
        # preorder[0] is root of cur tree, each time pop and get cur rooot
        root_v = preorder.pop(0)
        # create cur subtree based on cur root
        root = TreeNode(val=root_v)
        # define left,right subtree
        mid = inorder.index(root_v)
        # assign root.left, root.right node from recursion
        root.left = self.buildTree(preorder, inorder[:mid])
        root.right = self.buildTree(preorder, inorder[mid+1:])

        # return cur node
        return root


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
