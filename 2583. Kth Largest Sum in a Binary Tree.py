# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    """
    Question: Use Minheap + BFS
    """
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return -1
        res = []
        level = 0

        def bfs(node):
            nonlocal level
            # use queue to store node at each level
            q = deque([node])
            while len(q) > 0:
                # iterate q 
                i,size = 0,len(q)
                tot = 0
                while i < size:
                    tot += q[i].val
                    i+= 1
                res.append(tot)

                while size > 0:
                    cur = q.popleft()
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                    size -= 1
                level += 1

        bfs(root)
        return self.get_kth(res, k) if level >= k else -1
    
    def get_kth(self, res: List[int], k: int) -> int:
        # use minheap
        heap = []
        for n in res:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]