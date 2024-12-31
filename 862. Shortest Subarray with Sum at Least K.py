class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Keep increasing stack: shortest length of subarray which sum >= k
        # sum[l,r] = prefixsum[r+1] - prefixsum[l]
        res = len(nums) + 1
        prefixsum = [0] * (len(nums) + 1) # make leading 0
        q = deque()
        # 1.compute prefixsum
        for i in range(len(nums)):
            prefixsum[i+1] = prefixsum[i] + nums[i]
        # iterate prefixsum
        for i in range(len(prefixsum)):
            # 2.already satisfy, count res
            # left pop
            while q and prefixsum[i] - prefixsum[q[0]] >= k:
                first = q.popleft()
                res = min(res, i-first)
            # 3.handle enqueue
            # right pop
            # keep increasing queue, if see smaller ,pop since shorter subarray
            while q and prefixsum[i] <= prefixsum[q[-1]]:
                q.pop()
            # 4.push cur
            q.append(i)

        return res if res != len(nums) + 1 else -1