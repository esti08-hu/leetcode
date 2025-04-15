"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: list["Employee"], id: int) -> int:
        
        employee_map = {employee.id: employee for employee in employees}
        
        def dfs(employee_id: int) -> int:
            employee = employee_map[employee_id]
            totoal_imp = employee.importance

            for sub_id in employee.subordinates:
                totoal_imp += dfs(sub_id)
            return totoal_imp
        
        return dfs(id)