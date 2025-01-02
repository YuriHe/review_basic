from typing import (
    List,
)

class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    """
    Question:return modified array after index-value updates 
    Topic:update start, end+1 index, prefixsum to roll sum
    """
    def get_modified_array(self, length: int, updates: List[List[int]]) -> List[int]:
        # Write your code here
        res = [0] * length
        # fill out res ls based on updates, +value at start point, -value at next of end point
        # if end already last one, no need action
        for update in updates:
            start = update[0]
            end = update[1]
            inc = update[2]
            res[start] += inc
            if end >= length-1:
                continue
            else:
                res[end+1] -= inc
        
        prefix = 0
        for i in range(len(res)):
            prefix += res[i]
            res[i] = prefix
        return res
