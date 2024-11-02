# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: combine digits from root to leaf and sum up all branches
    SOLUTION1: Iterate tree via BFS, accumulate to cur val, modify each node value
    PATTERN: BFS->deque->no need level count, so not nested while, each val will based on their latest ancestor -> DFS
    """
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # collect res when they are leaves
        res = 0
        q = deque([root])
        while len(q) > 0:
            out = q.popleft()
            node_v = out.val
            if out.left:
                out.left.val += node_v * 10
                q.append(out.left)
            if out.right:
                out.right.val += node_v * 10
                q.append(out.right)
            if not out.left and not out.right:
                # it is leaf, count to res
                res += out.val
        return res
    

    # SOLUTIN2: dfs
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur_sum):
            if not node:
                return 0
            cur = cur_sum * 10 + node.val
            if not node.left and not node.right: # it is leaf
                return cur
            return dfs(node.left, cur) + dfs(node.right, cur)
        return dfs(root, 0)
            