"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
"""
Question: deserialize quad tree from 2D to tree,each layer divde n/2,n/4 until1, H is logn,totalT:n*n*logn
1Step:root isn't any cell, think whole, dfs(n, r, c)=>dfs(len(grid),0,0)
2Step:inside dfs(one quad),nested loop check if they are same, if yes, leaf; else divide again
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            allSame = True
            value = grid[r][c]
            # increment part
            for i in range(n):
                for j in range(n):
                    if grid[r+i][c+j] != value:
                        allSame = False
                        break # break no continue, need divide later
            if allSame:
                # topleft,right,.. are None
                return Node(value, True)
            # need keep divide
            half = n // 2
            topLeft = dfs(half, r, c)
            topRight = dfs(half, r, c + half)
            bottomLeft = dfs(half, r + half, c)
            bottomRight = dfs(half, r + half, c + half)
            return Node(value, False, topLeft, topRight, bottomLeft, bottomRight)


        return dfs(len(grid), 0, 0)