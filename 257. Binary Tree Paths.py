# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: return all path from root to leaf
    Topic: DFS recursion
    """
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []
        res = []
        # use recursion helper
        self.dfs(root, "", res)
        return res
    
    def dfs(self, root, path, res):
        path += str(root.val)
        # base case: leaf
        if not root.left and not root.right:
            res.append(path)
            return
        if root.left:
            self.dfs(root.left, path+"->", res)
        if root.right:
            self.dfs(root.right, path+"->", res)
