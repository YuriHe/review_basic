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
    
    def dfs(self, root, tmp, res):
        if not root:
            return
        tmp += str(root.val)
        if not root.left and not root.right:
            # it is leaf
            res.append(tmp)
        if root.left:
            self.dfs(root.left, tmp+"->", res)
        if root.right:
            self.dfs(root.right, tmp+"->", res)