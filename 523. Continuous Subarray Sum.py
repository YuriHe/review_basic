class Solution:
    """
Question:Ask if exist subarray where sum is multiple of k
Topic:prefixsum[j]%k=prefixsum[i]%k
Step1:hashmap store {modval:index} index because can count length to i
Step2:valaid >=2 length subarray when check i - modmap[remainder] >=2
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums: return 0

        mod_map = {} # store modV:idex
        mod_map[0] = -1 # since we need at least two ele, avoid 1ele divisible by k is counted
        prefixsum = 0
        for i in range(len(nums)):
            prefixsum += nums[i]
            remainder = prefixsum % k
            if remainder < 0:
                remainder += k # in case input have negative
            if remainder in mod_map:
                # if yes now check length
                if i - mod_map[remainder] >= 2:
                    return True
                # wait more eles
            else:
                mod_map[remainder] = i
        return False


