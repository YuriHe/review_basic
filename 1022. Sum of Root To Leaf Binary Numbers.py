# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # store binary strings of all branches from root to leaf
        self.branch = []
        
        def traverse(node, cur):
            if not node: return
            cur += str(node.val)
            if not node.left and not node.right:
                self.branch.append(cur[:])
                return
            traverse(node.left, cur)
            traverse(node.right, cur)

        traverse(root, "")

        # handle branch list, convert binary string to digit number
        res = 0
        for b in self.branch:
            res += int(b,2)
        return res
        # OR
        return sum(int(b,2) for b in self.branch)
