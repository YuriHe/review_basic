class Solution:
    """
    Question: Subarray Sum Equals K
    TOPIC: prefix sum, STEP:DONT USE SLIDING WINDOW SINCE positive/negative
    STEP: store (subtotal, appear_times) to map
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = dict()
        # for check sub_total-k = 0 in map
        dic[0] = 1
        res = 0
        sub_total = 0
        for n in nums:
            sub_total += n
            if sub_total - k in dic: # =0, or extra already visited
                res += dic[sub_total-k]
            dic[sub_total] = dic.get(sub_total, 0) + 1 # appears again, count 1
        return res
            