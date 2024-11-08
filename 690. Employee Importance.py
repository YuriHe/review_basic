"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # create hashmap id:[important, subs]
        people = {}

        # fill people dict
        for p in employees:
            people[p.id] = [p.importance, p.subordinates]

        # find id 
        res = people[id][0]

        def dfs(subs):
            nonlocal res

            if not subs: return
            for sub in subs:
                res += people[sub][0]
                dfs(people[sub][1])
        # go to subs
        dfs(people[id][1])
        return res
        