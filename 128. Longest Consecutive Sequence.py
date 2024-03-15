class Solution:
    """
    Question: find longest consecutive sequence in nums list, num: positive,negative
    SOLUTION1: BRUTE FORCE O(n^2)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        # SOLUTION: BRUTE FORCE O(n^2)
        if not nums: 
            return 0
        num_set = set(nums)
        res = 0
        for n in num_set:
            # check if num - 1 is in the set, if not, it's the start of a sequence
            if n-1 not in num_set:
                cur_num = n
                cur_len = 1

                # increment current_num until consecutive numbers are not in the set
                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_len += 1

                # update len
                res = max(res, cur_len)   
        return res

