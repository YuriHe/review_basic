"""
    Question: find highest frequency of element in the list
    Issue: element that appears more than ⌊n / 2⌋ times
    Solution1: Sort, majority ele's index >= [n/2] after sorted
    Solution2: Hashmap
    Followup: linear time and in O(1) space
    Solution3: Boyer-Moore Voting Algorithm T:O(n);S:O(1)
"""
def majorityElement(self, nums: List[int]) -> int:
    # Solution1: T:O(nlogn), S: O(1)
    nums.sort()
    return nums[len(nums) // 2]
    # Solution2:  T: O(n), S: O(n)
    dic = {}
    for n in nums:
        dic[n] = dic.get(n, 0) + 1
    maxi_k_v = [None, None]
    for k, v in dic.items():
        if maxi_k_v[0] is None or v > maxi_k_v[1]:
            maxi_k_v = [k, v] # update k, v 
    return maxi_k_v[0]
    # Solution2.2
    from collections import Counter
    count_dict = Counter(nums)
        ele = [None, 0]

        for c, ct in count_dict.items():
            if ele[0] is None or ct >= ele[1]:
                # update ele dict
                ele = [c,ct]
        
        return ele[0]
    # Solution3: 
    candidate = 0
    count = 0
    for n in nums:
        if candidate == n:
            count += 1
        else:
            if count == 0: # now val is not cur candidate
                candidate = n
                count += 1
            else:
                # now new val 
                count -= 1
    return candidate
