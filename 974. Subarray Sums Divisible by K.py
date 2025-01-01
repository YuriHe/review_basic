class Solution:
    # Question:return number of subarray sum %k=0
    # Topic:(prefixsum[j]-prefixsum[i]) mod k=0->prefixsum[j] mod k = prefixsum[i] mod k
    # 
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 1
        res = 0
        prefixsum = 0
        for i in range(len(nums)):
            prefixsum += nums[i]
            remainder = prefixsum % k
            if remainder < 0:
                remainder += k
            if remainder in dic:
                res += dic[remainder]
            dic[remainder] += 1
        return res
