"""
    Question:min cost for climb starts with 1/2 steps, start 0 or 1index
"""
def minCostClimbingStairs(self, cost: List[int]) -> int:
    # cost list["0->1step cost", "1->2step cost"]
    # add value in the end
    cost.append(0)
    for i in range(2, len(cost)):
        cost[i] += min(cost[i-1], cost[i-2])
    return cost[-1]