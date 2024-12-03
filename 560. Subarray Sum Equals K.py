class Solution:
    """
    Question: return total number of subarrays who sum = target
    1.count all subarray sum = target => prefix sum, not sliding window
    2.presum[i] = presum[j](in dict) + k, update dict[presum[i] - k] = occurance
    ! Not use sliding window since probably negative number and dynamic boundry
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        # check prefix sum check prefixsum - target in hashmap 
        # hashmap {prefixsum: count}
        dic = defaultdict(int)
        # default 0: 1
        dic[0] = 1
        prefixsum = 0
        res = 0

        for n in nums:
            prefixsum += n

            if prefixsum - k in dic:
                res += dic[prefixsum - k]

            dic[prefixsum] += 1

        return res