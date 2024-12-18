"""
339. Nested List Weight Sum
given a nestedList consisting of integers that might be wrapped in multiple layers of lists. 
An integer's depth is determined by how many lists contain it. 
For instance, in the list [1,[2,2],[[3],2],1], the number 1 is at depth 1 (since it's not within any nested list), the number 2 is at depth 2 (as it is in one nested list), and the number 3 is at depth 3 (as it's in two nested lists).
[1,[4,[6]]]
output is 1*1+4*2+6*3=27
each integer multiple * their depth and sum them up
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    """
    Question: DFS
    """
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # recursion传变量
        def dfs(ls, depth):
            res = 0
            for item in nestedList:
                if item.isInteger():
                    # get this value times * current depth
                    res += item.getInteger() * depth
                else:
                    # recursively call 
                    res += dfs(item.getList(), depth + 1)
            return res

        return dfs(nestedList, 1)


    def depthSumInverse2(self, nestedList: List[NestedInteger]) -> int:
        def get_max_height(ls):
            height = 1
            for item in ls:
                if not item.isInteger():
                    height = max(height, get_max_height(item) + 1)
            return height


        # recursion传变量
        def dfs(ls, depth):
            res = 0
            for item in nestedList:
                if item.isInteger():
                    # get this value times * current depth
                    res += item.get_max_height() * depth
                else:
                    # recursively call 
                    res += dfs(item.getList(), depth-1)
            return res
        
        h = get_max_height(nestedList)
        return dfs(nestedList, h)
