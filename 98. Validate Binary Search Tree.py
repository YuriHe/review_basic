# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Validate BST(unique num)
    SOLUTION1: inorder traversal to generate list and compare with sort list O(nlogn) and also need to check counter
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ls = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            ls.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        ctn_map = collections.Counter(ls)
        if all (v == 1 for v in ctn_map.values()) and ls == sorted(ls):
            return True
        else:
            return False

    """
    SOLUTION2: use dfs recursion
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')

        def dfs(node) -> bool:
            nonlocal prev

            if not node:
                return True
            # iterate left
            if not dfs(node.left):
                return False
            # computing
            if prev >= node.val:
                return False
            # update prev to cur node
            prev = node.val
            # iterate right
            if not dfs(node.right):
                return False
            # DONE consider all egdes
            return True
        
        return dfs(root)

    """
    SOLUTION3: use iterative function by using stack  (BEST)
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
            # create stack list store node
            stack = []
            # traverse tree
            cur = root
            # set ancestor 
            prev = float('-inf')

            while cur or stack:
                # go leftmost nodes
                while cur:
                    stack.append(cur)
                    cur = cur.left
                # go to first smallest node
                cur = stack.pop()
                if prev >= cur.val:
                    return False
                # update prev
                prev = cur.val

                # move to right subtree
                cur = cur.right
            
            return True
