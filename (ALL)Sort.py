# Topological Sort
# Directed graph
# 1way: Use BFS Kahn algorithm
# 2way: Use DFS
"""
1 Problem: Calculate the Minimum Total Time to Complete All Tasks Given Durations and Dependencies
Description: You are tasked with scheduling several tasks. Each task has an execution time, and there are dependencies between some tasks, meaning that certain tasks must be completed before others. You need to calculate the minimum total time required to complete all tasks.
Input:
An integer n representing the number of tasks.
An integer array times, where times[i] represents the time required to complete task i.
A 2D array prerequisites, where prerequisites[i] = [a, b] indicates that task a must be completed before task b, i.e., task a is a prerequisite for task b.
Output:
Return the minimum total time required to complete all tasks.
Use BFS
"""
from collections import deque, defaultdict

def shortestTimeToFinishTasks(n, times, prerequisites):
    neighbors = defaultdict(list)
    finished_time = [0] * n
    indegree = [0] * n

    for pre, cur in prerequisites:
        neighbors[pre].append(cur)
        indegree[cur] += 1
    
    # fill q, store(task i, time)
    q = deque([]) 
    completed = 0
    for i in range(n):
        if indegree[i] == 0:
                # no prerequisite,execute task
                q.append(i)
                finished_time[i] = times[i]


    while len(q) > 0:
        first = q.popleft()
        completed += 1
        for i in neighbors[first]:
            indegree[i] -= 1
            # update finished time
            # when finish in parallel
            finished_time[i] = max(finished_time[i], finished_time[first] + times[i])

            if indegree[i] == 0: # no preq
                # push into q
                q.append(i)



    print(completed)
    print(finished_time)
    return max(finished_time) if completed == n else -1

n = 6
times = [2, 3, 2, 1, 4, 2]
prerequisites = [[0, 2], [1, 2], [2, 3], [3, 4], [4, 5]]

print(shortestTimeToFinishTasks(n, times, prerequisites))  # Output: 12