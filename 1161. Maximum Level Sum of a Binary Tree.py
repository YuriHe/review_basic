# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: find maxium sum of one layer in bt, if have multiple same sum, choose smaller layer(near root)
    BFS
    return level
    """
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        q = deque([root])
        res = []
        layer = 1
        while len(q) > 0:
            total = 0
            for n in q:
                total += n.val
            res.append((total,layer))

            size = len(q)
            while size > 0:
                first = q.popleft()
                if first.left:
                    q.append(first.left)
                if first.right:
                    q.append(first.right)
                size -= 1
            layer += 1
        maxv = float("-inf")
        maxl = 1
        for n, l in res:
            if n > maxv:
                maxv = n
                maxl = l
        return maxl



            
        