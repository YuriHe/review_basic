class Solution:
    """
    Question: return total number of subarrays who sum = target
    1.count all subarray sum = target => prefix sum, not sliding window
    2.presum[i] = presum[j](in dict) + k, update dict[presum[i] - k] = occurance
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = dict()
        # [k] k scene or [1,1,1] k=2, {1:1,2:1(2-k=0),3:1}
        freq[0] = 1
        presum = 0
        res = 0

        for n in nums:
            presum += n
            if presum - k in freq:#accumulate res from previous subarrays which sum had k, end with n
                res += freq[presum-k]
            freq[presum] = freq.get(presum, 0) + 1

        return res