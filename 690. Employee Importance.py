"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    """
    Question: get all importance value for itself and its direct/indirect subordinaries
    TOPIC: DFS
    T:O(N)
    S:O(N)
    """
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        all_id_to_employee = {employee.id: employee for employee in employees}
        return self.dfs(id, all_id_to_employee)
    
    def dfs(self, id: int, all_id_to_employee: dict) -> int:
        values = all_id_to_employee[id].importance
        for subId in all_id_to_employee[id].subordinates:
            values += self.dfs(subId, all_id_to_employee)
        return values
        