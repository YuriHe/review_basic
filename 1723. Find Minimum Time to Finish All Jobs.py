class Solution:
    """
    Question: minimum time to distribute all jobs(maximum working) for k workers
    Topic: Basic backtrack dfs(jobs_idx)+prune
    Step1:prune work heaviest first;prune not better res; prune symmetry job
    """
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # result get minimum finish time
        res = float('inf')
        # worker workload 
        load = [0] * k
        # Prune1: sort, job heaviest first
        jobs.sort(reverse=True)

        # dfs, use job's index dfs to see which workder handle
        def dfs(idx):
            nonlocal res
            # base case
            if idx == len(jobs):
                res = min(res, max(load))
                return
            for i in range(len(load)):
                # Prune2: assign job to this worker cannot improve res
                if load[i] + jobs[idx] >= res:
                    continue
                # Prune3: if assign to duplicate job. [3,3,2]k=2, [3,0],[0,3]is same
                if i > 0 and load[i] == load[i-1]:
                    continue
                load[i] += jobs[idx]
                dfs(idx+1)
                load[i] -= jobs[idx]

        dfs(0)
        return res
        