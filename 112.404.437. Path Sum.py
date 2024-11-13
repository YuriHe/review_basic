# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    112. Path Sum
    Question: if there is root-leaf path can sum up to targetSum
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and targetSum - root.val == 0: 
            return True
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val) 


class Solution:
    """
    404. Sum of Left Leaves
    """
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node: return
            if node and node.left and not node.left.left and not node.left.right:
                # find left leaf
                res += node.left.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return res


class Solution:
    """
    437. Path Sum III
    Question: if any parent node to child node can sum up to target
    prefix sum(560) + backtracking
    4,4,4  target 8 -> 0:1, 4:1, 8:2 12:2
    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        freq = defaultdict(int)
        freq[0] = 1 # prefix-targetsum in freq 

        def dfs(node, prefix):
            nonlocal res
            if not node:
                return
            # add cur to prefix sum
            prefix += node.val
            # check if meet targetsum, if yes, update res
            if prefix - targetSum in freq:
                res += freq[prefix-targetSum]
            # count prefix += 1 in map
            freq[prefix] += 1 

            # recursion
            dfs(node.left, prefix)
            dfs(node.right, prefix)

            # backtrack reset
            freq[prefix] -= 1

        dfs(root,0) # have prefix because count sum in each path
        return res