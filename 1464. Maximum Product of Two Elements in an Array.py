from heapq import nlargest
class Solution:
    '''
    QUESTION: return one largest value from (num[i]-1)*(num[j]-1), i and j are diff index, all nums are positive
    '''
    # SOLUTION1: heap behavior
    # TIME: O(n) TIME: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        return prod(x - 1 for x in nlargest(2, nums))

    # SOLUTION2: search firstlargest and secondlargest
    # TIME: O(n) TIME: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        firstlargest, secondlargest = -1, -1
        for n in nums:
            if n > secondlargest:
                secondlargest = n
            if secondlargest > firstlargest:
                temp = firstlargest
                firstlargest = secondlargest
                secondlargest = temp
        return (firstlargest -1) * (secondlargest-1)
        