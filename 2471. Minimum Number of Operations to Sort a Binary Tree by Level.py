# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    layer order bfs
    sort list via swap? -> create dict[level]=ls handle outside from queue, when iteratin queue
    value is unique, no duplicate
    no need to actually swap value, only need count
    push next level's nodes
    """
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 0
        q = deque([root])
        dic = collections.defaultdict(list)
        level = 0

        while q:
            size = len(q)
            for _ in range(size):
                first = q.popleft()
                dic[level].append(first.val)
                if first.left:
                    q.append(first.left)
                if first.right:
                    q.append(first.right)
            level += 1
        
        for ls in dic.values():
            x = sorted(ls)
            diff = 0
            for i in range(len(ls)):
                if ls[i] != x[i]:
                    # find index for correct value
                    j = ls.index(x[i])
                    ls[i], ls[j] = ls[j], ls[i]
                    diff += 1
            res += diff

        return res


                


