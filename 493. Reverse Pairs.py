class Solution:
    """
    limit is 
    i < j, but nums[i] > 2 * nums[j]
    Use merge sort, i from left subarray, j from right subarray 
    nlogn
    Divide the array into smaller subarrays.
    Conquer by counting reverse pairs in each subarray and across subarrays.
    Merge the subarrays back while maintaining the sorted order.
    """
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(start, end):
            if start >= end:
                #subaray no ele or 1 ele, cannot contain reverse pair
                return 0
            
            mid = start+(end-start) // 2
            # left half nums[start...mid] right half:nums[mid+1, end]
            count = merge_sort(start, mid) + merge_sort(mid + 1, end)

            # Count reverse pairs in and across subarray
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            # Merge the two halves
            temp = []
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1
            
            for i in range(len(temp)):
                nums[start + i] = temp[i]
            return count
            
        
        return merge_sort(0, len(nums) - 1)

        