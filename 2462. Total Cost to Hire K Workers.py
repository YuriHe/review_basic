class Solution:
    """
    Question: get total minium cost to hire k workers
    k is number we need to hire
    candidates = num, means can choose first num and last num
    create heap store(cost, index) which will automatically sort cost then index 
    if want to sort cost and index in descend order: heapq.heappush(heap, (cost, -index))
    use two pointer keep add
    """
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        res = 0
        heapL = []
        heapR = []
        i, j = 0, len(costs)-1 # next one from both sides

        for _ in range(k):
            while len(heapL) < candidates and i <= j:
                heapq.heappush(heapL, (costs[i], i))
                i += 1
            while len(heapR) < candidates and i <= j:
                heapq.heappush(heapR, (costs[j], j))
                j -= 1
            if not heapL:
                res += heapq.heappop(heapR)[0]
            elif not heapR:
                res += heapq.heappop(heapL)[0]
            elif heapL[0][0] <= heapR[0][0]:
                res += heapq.heappop(heapL)[0]
            else:
                res += heapq.heappop(heapR)[0]
        return res
            

