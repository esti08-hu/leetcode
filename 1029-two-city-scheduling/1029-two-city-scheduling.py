class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        const_sorted = sorted(costs, key=lambda x: x[0] - x[1])

        n = len(costs)//2
        res = []
        for a,b in const_sorted[:n]:
            res.append(a)

        for a,b in const_sorted[n:]:
            res.append(b)

        return (sum(res))
