"""
    Question: whenever you are finding continous elements then keep them in an interval else make them alone. diff = num[i]-nums[i-1], if diff==1, in same interval
"""
def summaryRanges(self, nums: List[int]) -> List[str]:
    res = []
    i = 0
    while i < len(nums):
        start = nums[i]
        # find rest of nums until not diff != -1
        while i + 1 <len(nums) and nums[i+1] - nums[i] == 1:
            i += 1
        # find interval only return start->end
        if start != nums[i]:
            res.append(str(start)+"->"+str(nums[i]))
        else:
            # only one ele in this interval
            res.append(str(start))
        i += 1
    return res
