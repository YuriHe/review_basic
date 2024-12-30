class Solution:
    """
    exact k transfer to atmost(k) - atmost(k-1)
    [1,2,3]
    all subaray:[1].[2],[3].[1,2],[2,3],[1,2,3] , total is 6 number of subaray same as n*(n+1)/2:1+2+3+...+n
    If left = 2 and right = 4, the subarrays are [2:5], [3:5], [4:5] → 3 subarrays.
    """
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(v):
            # return number of sbuarray at at most K odd number
            res, left, odd = 0,0,0
            for right in range(len(nums)):
                # only odd will have 1 else 0
                # 1.add
                odd += nums[right] % 2
                # 2.invalid window
                while odd > v:
                    leftn = nums[left]
                    odd -= leftn % 2
                    left += 1
                # 3.valid
                # number n , will get n*(n+1)/2=1+2+3+....+n subarray
                # nums[left:right+1], nums[left+1:right+1], ..., nums[right:right+1]
                # number of valid subarrays ending at right
                res += right-left+1
            return res

        return atMost(k) - atMost(k-1)
        