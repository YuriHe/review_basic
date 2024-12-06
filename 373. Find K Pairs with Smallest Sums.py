class Solution:
    """
    Question: find K pairs with smallest sums from two arrays
    Maxheap + combination
    """
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        #  make combination from nums1 and nums2 and store all
        heap = [] # (sum, n1, n2)
        for n1 in nums1:
            for n2 in nums2:
                tmp = n1 + n2
                if len(heap) < k:
                    heapq.heappush(heap, (-tmp, n1, n2))
                else:
                    if -heap[0][0] > tmp:
                        heapq.heappop(heap)
                        heapq.heappush(heap, (-tmp, n1, n2))
                    else:
                        # nothing
                        break

        # fetch rest of heap with k size
        res = [[n1, n2] for _, n1, n2 in heap]
        return res
        
                
