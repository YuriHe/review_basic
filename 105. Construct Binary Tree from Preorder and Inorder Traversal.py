# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        SOLUTION1: Recursion 
        TIME:O(n^2)because find index; SPACE: O(n)
        """
        # base case
        if len(inorder) == 0:
            return None
        # build tree
        # first node in preorder is root, use inorder to subtree
        root = TreeNode(val=preorder.pop(0))
        # recursively call inorder array
        rootIdx = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:rootIdx])
        root.right = self.buildTree(preorder, inorder[rootIdx+1:])
        return root
        """
        SOLUTION2: Recursion + hashmap
        hashmap store inorder v: index, so use hashmap can find index then split tree into half
        TIME: O(n), SPACE O(n)
        """
        in_map = {v:i for i, v in enumerate(inorder)}
        
        preorder_idx = 0

        def dfs(l, r):
            nonlocal preorder_idx
            if l > r:
                return None

            # get every subtree's root 
            value = preorder[preorder_idx]
            preorder_idx += 1
            # create tree node
            root = TreeNode(val=value)
            mid = in_map[value]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root

        return dfs(0, len(inorder)-1)
        