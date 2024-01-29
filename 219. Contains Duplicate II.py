"""
    Question: check if nums[i]=nums[j], and abs(i-j) <= k
    Solution1: Use map store{num, index}
"""
def containsNearbyDuplicate(nums, k):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic and abs(i- dic[nums[i]] ) <= k: return True
        else:
            dic[nums[i]] = i
    return False

print(containsNearbyDuplicate([1,0,1,1], 1))