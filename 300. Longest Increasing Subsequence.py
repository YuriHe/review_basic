class Solution:
    """
    Question: return length of longest strictly increasing subsequence 
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        1SOLUTION: bottom-up DP + Two pointer
        TIME: O(n^2), SPACE: DP O(n)
        IDEA: two nested loop, outerloop using right pointer to track, 
        innerloop check subsequence starting from 0 and end with right pointer
        eg.[2,5,7]
        dp right=0, [1,1,1]=>right=1, [1,2] => right=2, [1,2,3]
        """
        # create n size, default is 1 which means length=1 (one num)
        dp = [1] * len(nums)
        res = 1

        # two nested loop, update dp[i] present length of longest seq end at i
        for right in range(len(nums)):
            for left in range(0, right+1, 1):
                if nums[left] < nums[right]:
                    # it is part of valid seq
                    dp[right] = max(dp[right], dp[left] + 1)
                res = max(res, dp[right])
        return res

        """
        2SOLUTION:Binary search (HARD)
        TIME:O(nlogn)
        eg.[0,1,0,3,2,3]
        seq=[0,1], 0 replace with 0 => [0,1,3]=> [0,1,2] replace 3 with 2 => [0,1,2,3]
        """
        # store smallest possible for strictly increasing sequence
        seq = []
        seq.append(nums[0])

        def _binary(target):
            # find pos to replace by target, pos is first index in `seq` where `seq[pos] >= target`
            low, hi = 0, len(seq)-1
            while low < hi:
                mid = (low+hi)//2
                if seq[mid]<target:
                    low = mid+ 1
                else:
                    hi = mid
            return low

        for i in range(1, len(nums)):
            if nums[i] > seq[-1]:
                seq.append(nums[i])
            else:
                # find the pos replace target since smaller value allow more room to become longest seq
                pos = _binary(nums[i])
                seq[pos] = nums[i]
        return len(seq)

        