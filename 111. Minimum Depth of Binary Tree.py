# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: find minimum depth of bt
    if skewed tree, all nodes are on one branch
    cannot compeletely copy maximum depth of bt
    minimum depth need to compare all paths to leaf
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 1SOLUTION: recursion O(n) but have stack space O(logn)
        if not root:
            return 0
        # If only one child is present, go down the path of the other child
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        # If both children are present, take the minimum depth of both subtrees
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        # 2SOLUTION: bfs O(n)
        if not root: return 0
        q = deque([root])
        depth = 1
        while q:
            size = len(q)
            for _ in range(size):
                first = q.popleft()
                # meet target
                if not first.left and not first.right: return depth
                if first.left:
                    q.append(first.left)
                if first.right:
                    q.append(first.right)
            depth += 1
        return - 1