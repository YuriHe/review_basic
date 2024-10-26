class Solution:
    """
    Question: use each integer(+ or - before it) in nums list and concatenate all the integers
    There is two options: +, - and finally got target
    Top-down recursion
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # SOLUTION1 use cache  T: n^2
        @cache
        def rec(index, remaining):
            # base case 
            if index == len(nums):
                return 1 if remaining == 0 else 0
            # choose addition
            add = rec(index+1, remaining-nums[index])
            # choose subtraction
            sub = rec(index+1, remaining+nums[index])
            return add + sub

        return rec(0, target)

        # SOLUTION2 use memorization, maximum depth of recurision stack is O(n), T:O(n*S) with memorization. S is the sum of all numbers in nums (the maximum possible range of remaining). 
        # use (index, remaining) is memo's key because that is unique when handle addition/substraction
        memo = {}
        def rec(index, remaining):
            # base case
            if index == len(nums):
                return 1 if remaining == 0 else 0
            # check memo
            if (index, remaining) in memo:
                return memo[(index, remaining)] # pull out result from memo, memo[(index, remaining)] = ways of combination so far
            # addition
            add = rec(index+1, remaining - nums[index])
            # subtraction
            sub = rec(index+1, remaining + nums[index])
            # store to memo
            memo[(index, remaining)] = add+sub
            return add + sub

        return rec(0, target)





        