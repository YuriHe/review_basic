# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: sum up all val in [low, high]
    TOPIC: iterate BST 
    """
    # SOLUTION1: inorder traverse
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0

        def inorder(node):
            nonlocal total
            if not node: return
            inorder(node.left)
            if low<= node.val and node.val<=high:
                total += node.val
            inorder(node.right)

        
        inorder(root)
        return total

        
    # SOLUTION: BFS
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        q = deque([root])
        while len(q) > 0:
            out = q.popleft()
            if out.val >= low and out.val <= high:
                res += out.val
            if out.left:
                q.append(out.left)
            if out.right:
                q.append(out.right)

        return res
    