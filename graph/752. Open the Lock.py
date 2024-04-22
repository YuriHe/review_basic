class Solution:
    """
    Question:Minimum step to reach targetxxxx from 0000, avoid getting value in deadends
    also each time only turn one wheel. 0 - 9
    TODO:
    1.use BFS with memorization find shortest path in unweighted graph
    2.use set to store deadends instead of array, retrieve O(1)
    3.use operation UP, DOWN to determine next state
    Complexity: S(10^n), T(1)
    """
    def _get_next_state(self, lock, index, operation):
        lock = list(lock)
        if operation == "UP":
            if lock[index] == "9":
                lock[index] = "0"
            else:
                lock[index] = str(int(lock[index]) + 1)
        else:
            if lock[index] == "0":
                lock[index] = "9"
            else:
                lock[index] = str(int(lock[index]) - 1)
        return "".join(lock)

    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: return -1
        deadends = set(deadends)
        q = deque(["0000"])
        # store memorization dict which for return and keep track {cur_lock: cur_steps}
        visited = {"0000": 0}
        while len(q) > 0:
            first = q.popleft()
            # END CASE check if find target before explore neighbors
            if first == target:
                return visited[first]
            # check next state(8 neighbors for 4 digits)
            for i in range(4):
                for op in ["UP", "DOWN"]:
                    new_lock = self._get_next_state(lock=first, index=i, operation=op)
                    # if new_lock already visited, no need to append to q, since already had same path, just previous path enough
                    # if new_lock in deadends, no need to append to q, since this path not work 
                    if new_lock not in visited and new_lock not in deadends:
                        # update visited memorization dict
                        visited[new_lock] = visited[first] + 1
                        # add q
                        q.append(new_lock)
        return -1
                        
                    




        