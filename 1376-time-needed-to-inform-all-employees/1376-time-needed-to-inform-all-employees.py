class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = defaultdict(list)
        for emp_id, mgr_id in enumerate(manager):
            if mgr_id != -1: 
                tree[mgr_id].append(emp_id)

        def dfs(emp_id):
            if emp_id not in tree:
                return 0

            max_time = 0
            for sub_id in tree[emp_id]:
                max_time = max(max_time, dfs(sub_id))

            return informTime[emp_id] + max_time

        return dfs(headID)