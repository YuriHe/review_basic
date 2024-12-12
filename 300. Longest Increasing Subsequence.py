"""
    Question: longest increaseing subsequence(not continuous) of number
    1. Bottom-up DP
    two loops for find increasing subsequence at certain range
    return max(dp), this time, last value of dp is not anwser
"""
def lengthOfLIS(self, nums: List[int]) -> int:
    # 1SOLUTION: bottom-up DP
    # N^2
    # create dp array with nums size, default val is 1, since 1 val can be subsequence
    # at i index will present longest subsequence can get so far
    dp = [1] * len(nums)
    # return longest length of subsequence
    res = 1
    for i in range(1, len(dp)): # cur index(right)
        for j in range(0, i): # start of subsequence
            if nums[j] < nums[i]: # valid 
                dp[i] = max(dp[i], dp[j] + 1)
                res = max(res, dp[i])
    return res

    # 2 SOLUTION: construct subsequence
        # if cur > last of sub, append
        # else: replace val in sub, do loop to find big one since give more space to do increase subsequence,
        # why not pop last and insert, instead using loop: [4,10,4], avoid duplicate
        # N^2
        """
        [5,1,2,7,6,3]
         5
           1
           1,2
           1,2,7
           1,2,  6
           1,2,    3
    """
    sub = []
    sub.append(nums[0])
    
    for i in range(1, len(nums)):
        if nums[i] > sub[-1]:
            sub.append(nums[i])
        else:
            j = 0
            # search bigger than cur
            while sub[j] < nums[i]: 
                j += 1
            # find bigger than cur
            sub[j] = nums[i]
    return len(sub)

    # 3 SOLUTION: binary search based on solution2 construct subsequence
    sub = []
    sub.append(nums[0])
    def binary(target):
        # find pos to replace by target
        # pos is first pos that larger/equal to target
        low, high = 0, len(sub) - 1
        while low < high:
            mid = (low + high) // 2
            if sub[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

    for i in range(1, len(nums)):
        if nums[i] > sub[-1]:
            sub.append(nums[i])
        else:
            # through sorted sub array to binary search 
            # find first element in sub that is greater or equal to cur
            # why first larger since more room to build increasing consequence
            pos = binary(nums[i])
            sub[pos] = nums[i]
    return len(sub)


