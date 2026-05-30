class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total = sum(salary) - salary[-1] - salary[0]
        return total / (len(salary) - 2)