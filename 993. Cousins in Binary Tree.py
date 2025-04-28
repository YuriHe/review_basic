# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    QUESTION: check if x and y have different direct parents and same depth
    """
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        """
        SOLUTION1: BFS
        STEP:1.iterate whole tree looking for target x and y, once found, store(parent, depth)
        2.compare the parents and depth of two noodes found and get result
        """
        q = deque([(root, None, 0)]) # store (curnode, parentnode, depth)tuple
        match = [] # store {parent, depth} tuple for x, y
        while q:
            # minor optimization to stop early if both targets found
            if len(match) == 2:
                break
            cur, parent, depth = q.popleft()
            if cur.val == x or cur.val == y:
                match.append((parent, depth))
            if cur.left:
                q.append((cur.left, cur, depth+1))
            if cur.right:
                q.append((cur.right, cur, depth+1))
        xRes, yRes = match
        return xRes[0] != yRes[0] and xRes[1] == yRes[1] # different parent but same depth