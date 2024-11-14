# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Search a node, if not exist, return original tree; if yes, delete it
    """
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val > key:
            # go to left subtree
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            # go to right subtree
            root.right = self.deleteNode(root.right, key)
        else:
            # find node: root
            if not root.left and root.right:
                # return right subtree since no left
                return root.right
            elif root.left and not root.right:
                # return left subtree since no right
                return root.left
            elif not root.right and not root.right:
                # only node deleted
                return None
            else:
                # modify tree structure
                # keep rightsubtree same, and iterate rightmost in leftsubtree
                # reassign value 
                cur = root.left
                while cur.right:
                    cur = cur.right
                # cur replace deleted node, no real action(no need re-link)
                root.val = cur.val
                # Delete the duplicate node from the left subtree
                root.left = self.deleteNode(root.left, cur.val)
        return root 

