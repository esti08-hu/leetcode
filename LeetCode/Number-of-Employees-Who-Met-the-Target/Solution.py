1class Solution:
2    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
3        count = 0
4        for hour in hours:
5            if hour >= target:
6                count += 1
7        return count