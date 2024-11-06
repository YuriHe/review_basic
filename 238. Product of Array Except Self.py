class Solution:
    """
    Question: product of array except self, at i, will mulitple all number except num[i]
    SOLUTION1:brute force O(n^2) TLE
    SOLUTION2:division O(n)
    SOLUTION3:array
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # SOLUTION 1 Brute force
        prod = 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    prod *= nums[j]
            res[i] = prod
        return res

        # SOLUTION2 division
        zeroctn, prod = 0, 1
        res = [0] * len(nums)

        for n in nums:
            if n == 0:
                zeroctn += 1
            else:
                prod *= n # avoid * 0
            if zeroctn > 1:
                return [0] * len(nums) # exit early

        for i in range(len(res)):
            if zeroctn > 0:
                if nums[i] == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod //nums[i]
        return res
        
        # SOLUTION3
        left = [1] * len(nums) # can avoid zero
        right = [1] * len(nums)
        res = [0] * len(nums)

        for i in range(0, len(nums)-1):
            left[i+1] = left[i] * nums[i]
        for i in range(len(nums)-1, 0, -1):
            right[i-1] = right[i] * nums[i]
        for i in range(len(res)):
            res[i] = left[i] * right[i]
        return res

        
        
