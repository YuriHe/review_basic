"""
In this problem, there is an undirected graph with n nodes. 
There is also an edges array. Where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

You need to return the number of connected components in that graph.
eg1.
3 nodes(0,1,2)
[[0,1], [0,2]] -> 1
"""
from typing import (
    List,
)

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # create array filled out parent, itself is parent
        parent = [i for i in range(n)]
        # height of tree, itself is parent, so default 1 height
        rank = [1] * n

        # flatten tree | path compression
        def find(n1):
            res = n1

            # tree down toward to root, since root=parent(root)
            while res != parent[res]:
                # let res directly point to grandparent(root)
                parent[res] = parent[parent[res]] # for optimize
                res = parent[res]
            return res

        # union rank, attach smaller tree too larger oone
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else: # rank of p1 higher
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res


class Solution:
    """
    547. Number of Provinces
    Unionfind merge connected in undirect graph
    O(E+V)
    """
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [1] * n

        # find node
        def find(n):
            # travese up to tree and path compression
            cur = n
            while cur != parent[cur]: # until root
                # set parent to grandpa v
                parent[cur] = parent[parent[cur]]
                # update cur
                cur = parent[cur]
            return cur

        # union rank, attach smaller tree to larger one
        def union(n1, n2):
            f1, f2 = find(n1), find(n2)
            if f1 == f2: # same node or already in group
                return 0 # nothing to union
            
            # check rank
            # check if descendant n2 high than parent n1
            if rank[f2] > rank[f1]:
                parent[f1] = f2 # f2 is root
                rank[f2] += rank[f1]
            else:
                # parent higher or equal to descendant
                parent[f2] = f1
                rank[f1] += rank[f2]
            return 1

        # n node
        res = n
        # iterate 2d, pick i, j edge
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    res -= union(i, j)
        return res


        