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
        # 1SOLUTION: Queue bfs
        if root is None: return []
        q = collections.deque([root])
        res = []
        while q:
            inner = []
            size = len(q)
            for _ in range(size):
                first = q.popleft()
                inner.append(first.val)

                if first.left:
                    q.append(first.left)
                if first.right:
                    q.append(first.right)

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
            tmpsum = 0
            
            for _ in range(size):
                first = q.popleft()
                tmpsum += first.val
                if first.left:
                    q.append(first.left)
                if first.right:
                    q.append(first.right)
            
            # finish this layer pop+push, now count average
            res.append(tmpsum/size)
        return res

class Solution:
    """
    199. Binary Tree Right Side View
    Question: iterate bt and return list of valaue from right side view
    BFS, return last value in each layer
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root])
        res = []

        while q:
            size = len(q)
            res.append(q[-1].val)

            for _ in range(size):
                first = q.popleft()
                if first.left:
                    q.append(first.left)
                if first.right:
                    q.append(first.right)
        return res

class Solution:
    """
    103. Binary Tree Zigzag Level Order Traversal
    Question: zigzag bfs 2nd from right to left
    """
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return [] # required!

        res = []
        q = deque([root])
        is_left = True # toggle this var

        while len(q) > 0:
            size = len(q)
            inner = []
            # retrieve this level 
            if is_left:
                i = 0
                while i < size:
                    inner.append(q[i].val)
                    i += 1
                is_left = False
            else:
                j = size-1
                while j >= 0:
                    inner.append(q[j].val)
                    j -= 1
                is_left = True
            # pop/push next layer
            while size > 0:
                first = q.popleft()
                if first.left:
                    q.append(first.left)
                if first.right:
                    q.append(first.right)
                size -= 1
            res.append(inner)
        return res



"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    """
    117. Populating Next Right Pointers in Each Node II
    Question: add next right pointer in each layer
    return the modify tree which add next right pointer
    """
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root

        q = deque([root])
        while q:
            size = len(q)
            for i in range(size-1):
                if i < size-1 :
                    q[i].next = q[i+1] 
            # last index
            q[-1].next = None
            
            for i in range(size):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root
