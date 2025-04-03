class Solution:
    """
    QUESTION:return list of string that within one range if consecutive otherse, in new range
    """
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        SOLUTION1: create string
        HOW: compare the neighbors
        TIME: O(N)
        """
        if len(nums) == 0: return []
        if len(nums) == 1: return [str(nums[0])]
        res = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                # cloose prev range now
                if start != nums[i-1]:
                    tmp = str(start) + "->" + str(nums[i-1])
                else:
                    tmp = str(start)
                res.append(tmp)
                # create new range's start
                start = nums[i]

            # extra think if last ele
            if i == len(nums)- 1:
                if start != nums[i]:
                    tmp = str(start) + "->" + str(nums[i])
                else:
                    tmp = str(start)
                res.append(tmp)
        return res
    
    """
        SOLUTION2: two pointer intervals (Faster)
        HOW: divide groups like merge intervals
        TIME: O(n)[although see there 2 while loop, but when searching group already iterated] SPACE: O(1)
    """
        res = []
        i = 0
        while i < len(nums):
            # define start inside of loop, which means iterate until grouping
            start = nums[i]
            # guess if time to wrap
            while i+1 < len(nums) and nums[i+1] - 1 == nums[i]:
                i+= 1
            # now grouping
            if start != nums[i]:
                res.append(str(start)+"->"+str(nums[i]))
            else:
                res.append(str(start))
            
            i+=1
        return res