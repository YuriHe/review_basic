class Solution:
    """
    1SOLUTION: brute force n^3, i,iterate subarray and update max(subarray)
    """
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Deques to maintain the current window's min and max elements
        maxQ = deque()  # stores indices of elements in decreasing order
        minQ = deque()  # stores indices of elements in increasing order
        left = 0  # left pointer of the sliding window
        res = 0  # to store the length of the longest valid subarray
        
        for right in range(len(nums)):
            # Maintain the min deque: elements in increasing order
            while minQ and nums[right] <= nums[minQ[-1]]:
                minQ.pop()
            minQ.append(right)
            
            # Maintain the max deque: elements in decreasing order
            while maxQ and nums[right] >= nums[maxQ[-1]]:
                maxQ.pop()
            maxQ.append(right)

            # Ensure the difference between max and min in the window is <= limit
            while nums[maxQ[0]] - nums[minQ[0]] > limit:
                # have to move left first
                # Move the left pointer and pop the front elements if out of window
                left +=1
                if minQ[0] < left:
                    minQ.popleft()
                if maxQ[0] < left:
                    maxQ.popleft()
            
            # Update the result with the current valid window length
            res = max(res, right - left + 1)
        
        return res

