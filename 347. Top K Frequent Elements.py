import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1.Solution: Hashmap+sort
        Idea: use Counter, and sort dict based on value, get key(tuple list)
        Time: O(nlogn) Space: O(n)
        """
        ctn = Counter(nums)
        sorted_k_vlist = sorted(ctn.items(), key=lambda x : (-x[1],x[0]))
        res = []
        idx = 0
        while idx < k:
            res.append(sorted_k_vlist[idx][0]) # append key
            idx += 1
        return res
        """
        2.Solution:hashmap+minheap
        Idea: Counter, push (CounterVal, CounterKey) to minheap
        Time: O(nlogk) Space: O(n)
        """
        ctn = Counter(nums)
        minheap = []
        for n, freq in ctn.items():
            heapq.heappush(minheap, (freq, n))
            if len(minheap) > k:
                heapq.heappop(minheap)
        res = []
        for _ in range(k):
            _, n = heapq.heappop(minheap)
            res.append(n)
        return res
        """
        3.Solution:bucket
        Idea: use Counter, create bucket 2D bucket[freq]=num
        Time: O(n), Space: O(n)
        """
        # create 2d, bucket[freq]=[n1, n2]
        bucket = [[] for _ in range(len(nums)+1)] 
        ctn = Counter(nums)
        for n, freq in ctn.items():
            bucket[freq].append(n)
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for val in bucket[i]:
                res.append(val)
                if len(res) == k:
                    return res
        return res