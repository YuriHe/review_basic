# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: combine digits from root to leave and sum up all branches
    TOPIC: Iterate tree via BFS, accumulate to cur val, modify each node value
    PATTERN: BFS->deque->no need level count, so not nested while
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
    

        