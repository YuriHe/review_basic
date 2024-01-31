"""
    Question: Binary Tree find maximum depth
    Topic: DFS -> find maximum depth
    Solution1: DFS recursion
    T: O(numbers of nodes) for traversing
    S: O(height of nodes) for recursive stack
"""
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None: return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))