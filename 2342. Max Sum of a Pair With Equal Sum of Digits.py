class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        """
        1.Solution: Hashmap{sumdigit: [i1, i2]}
        Idea: pre-handle hashmap, store {sum:[idx]} when iterate nums
        Time: O(len(nums) * max(len(digit))) + O(n*nlogn)
        """
        dic = collections.defaultdict(list)
        for i in range(len(nums)):
            n = nums[i]
            curSum = 0
            while n > 0:
                curSum += n % 10 # sum up each digit
                n //= 10 # moving n to left
            dic[curSum].append(i)

        maxPair = 0 # nums[i] >= 1

        for k, v in dic.items():
            if len(v) >= 2:
                # total is same, but get list from index and sort in desc for original num
                tmp = []
                for i in v:
                    tmp.append(nums[i])
                tmp.sort(reverse=True)
                # pick first 2
                maxPair = max(maxPair, tmp[0]+tmp[1])
        return maxPair if maxPair != 0 else -1
        """
        2.Solution:Track top two largest value per digitSum
        Idea: {digitSum: (max1, max2)} at least max1 exist, max2=0 as default
        Time: O(n * D)
        """
        dic = collections.defaultdict(list)
        for num in nums:
            n = num
            curSum = 0
            while n > 0:
                curSum += n%10
                n //= 10
            # define default value from [max1, max2]
            if curSum not in dic:
                dic[curSum] = [0,0]
            # get current max1, max2, and compare with cur num, keep updating max1, max2
            d1, d2 = dic[curSum]
            if num > d1:
                d2 = d1
                d1 = num
            elif num > d2:
                d2 = num
            # updating to dic
            dic[curSum] = [d1, d2]
        maxRes = -1
        for d1, d2 in dic.values():
            if d2 != 0:
                maxRes = max(maxRes, d1+d2)
        return maxRes if maxRes != -1 else -1

