"""
Question:minimum number of work session(number * sessionTime) to finish All jobs
Step:handle session list, use sessionCount to diff new or exit
[4,4,4], sessionT:6
"""
def minSessions(tasks,sessionTime):
    # worse case res is n, since max(tasks)=sessionTime, need len(task) number of session
    res = len(tasks)
    # pre-setup session size <=14, may not use all slots
    sessions = [0] * len(tasks)
    # Prune1
    tasks.sort(reverse=True)
    
    def dfs(task_id, ctn):
        nonlocal res
        # Prune2
        if ctn >= res: return
        # base case
        if task_id == len(tasks):
            res = min(res, ctn)
            return
        # iterate session if exit then reuse it
        for i in range(ctn):
            if sessions[i]+ tasks[task_id] <= sessionTime:
                sessions[i] += tasks[task_id]
                dfs(task_id+1, ctn)
                sessions[i] -= tasks[task_id]
        
        # create new session
        sessions[ctn] += tasks[task_id]
        dfs(task_id+1, ctn+1)
        sessions[ctn] -= tasks[task_id]
        
    dfs(0,0)
    return res
# prune方法：
# 1.sort reverse
# 2.res求最小值，过程超过res，return
# 3.跳出duplicate，比如duplicate load

print(minSessions([4,4,4], 6))