# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question:872. Leaf-Similar Trees
    Use dfs - preoder to store all leaves into arrays and check two arrays is same or not. if yes, then return true
    """
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if (not root1 and root2) or (root1 and not root2) or (not root1 and not root2): 
            return False
        ls1 = []
        ls2 = []
        def dfs(node, ls):
            if not node:
                return
            if not node.left and not node.right:
                # it is leaf
                ls.append(node.val)
                return 
            dfs(node.left, ls)
            dfs(node.right, ls)

        dfs(root1, ls1)
        dfs(root2, ls2)

        return ls1 == ls2