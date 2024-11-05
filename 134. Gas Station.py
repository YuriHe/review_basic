class Solution:
    """
    Question:return start index if trave whole circuit otherwise -1
    1.total_gas < total_cost->no solution; otherwise handle tank
    2.update tank, start
    no need to handle if travel whole circuit or track i+k % n because 1.2.
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        start = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                # reset start
                tank = 0
                start = i+1

        if total_gas < total_cost:
            return -1
        return start
