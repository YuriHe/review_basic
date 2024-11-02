import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    102. Binary Tree Level Order Traversal
    Question: BT BFS(breadth first search), search level by level
    TOPIC: BFS=QUEUE
    q store layer's nodes
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        q = collections.deque([root])
        res = []
        while len(q) > 0:
            inner = []
            # define size first, otherwise size will change
            size = len(q)
            while size > 0:
                first = q.popleft()
                inner.append(first.val)
                if first.left: 
                    q.append(first.left)
                if first.right:
                    q.append(first.right)
                
                size -= 1
            # done one level
            res.append(inner)

        return res


class Solution:
    """
    637. Average of Levels in Binary Tree
    Question: get average from each level
    BFS, use extra space to store nested array
    """
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if not root:
            return res

        q = deque([root])
        while len(q) > 0:
            size = len(q) # represent this layer
            size_2 = size
            total = 0
            
            # store next layer 
            while size > 0:
                first = q.popleft()
                total += first.val
                if first.left:
                    q.append(first.left)
                if first.right:
                    q.append(first.right)
                size -= 1
            
            # finish this layer pop+push, now count average
            res.append(total/size_2)
        return res
