# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # reverse node in odd level, start from 0(even)
        # traverse level -> bfs
        # modify value from tree not node!
        # BFS O(n)
        level = 0
        q = deque([root])
        while q:
            size = len(q)
            if level % 2 != 0:
                l, r = 0, size-1
                while l < r:
                    q[l].val, q[r].val = q[r].val, q[l].val
                    l += 1
                    r -= 1
            
            for _ in range(size):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            level += 1

        return root
