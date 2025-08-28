class Solution:
    """
    Question:return start index if trave whole circuit otherwise -1
    1.total_gas < total_cost->no solution; otherwise handle tank
    2.update tank, start
    no need to handle if travel whole circuit or track i+k % n because 1.2.
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 1 SOLUTION: brute force TLE
        find possible start point among many and loop from start-end where end
        prefind gas[i] >= cost[i] put the list
        if tank=0 for cur index still can go to next station which have gas
        possible = []
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                possible.append(i)
        
        for i in range(len(possible)):
            tank = 0
            start = possible[i]
            # Start from the current start point
            tank += gas[start] - cost[start]
            for j in range(start+1, start+len(gas)):
                cur = j % len(gas)
                tank += gas[cur] - cost[cur]

                if tank < 0:
                    break
                        # find another start
            if tank >= 0:
                return start
        return -1
        # 2SOLUTION: greedy
        if sum(gas) < sum(cost): return -1 # impossible, otherwise can finish whole route
        start = 0 # start index starting from 0index
        tank = 0 # accumulate sum for gas tank 
        for i in range(len(gas)):
            tank += gas[i]-cost[i]
            if tank < 0:
                # reset tank 
                tank=0
                # cur start not work, move one
                start = i+1
        return start