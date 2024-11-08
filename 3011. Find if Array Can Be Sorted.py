class Solution:
    """
    Quesstion: verify if can sort
    swap adjacent -> bubble sort
    """
    def canSortArray(self, nums: List[int]) -> bool:
        if not nums: return False
        for i in range(len(nums)):
            need_swap = False
            for j in range(0, len(nums) - i - 1):
                if nums[j] <= nums[j+1]:
                    continue
                if bin(nums[j]).count('1') == bin(nums[j+1]).count('1'):
                    # swap
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    need_swap = True
                else:
                    return False
            # if cur iterate, no need to swap, exit early
            if not need_swap:
                break
            
        return True
