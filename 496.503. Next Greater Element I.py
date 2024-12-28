class Solution:
    """
    1 step handle stack and find greater in nums2 alone and use hashmap store result
    2 step iterate nums1 extract hashmap result
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = []
        res = []
    # find next greater
    for i in range(len(nums2)-1, -1, -1):
        while stack and nums2[i] >= stack[-1]:
            stack.pop()
        hashmap[nums2[i]] = stack[-1] if stack else -1
        stack.append(nums2[i])
            
        for n in nums1:
            greater = hashmap[n]
            res.append(greater)
        return res

    class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 503. Next Greater Element II
        # 1019. Next Greater Node In Linked List
        # circular -> think mod assume we have 2*n; use i%n target res
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2*n-1, -1, -1):
            while stack and nums[i%n] >= stack[-1]:
                stack.pop()
            res[i%n] = stack[-1] if stack else -1 # may replaced 
            stack.append(nums[i%n])
        return res