from typing import List
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        num_list = [edge[1] for edge in edges]

        # num_set = set(num_list)

        degree = [-1]*(n)
        
        for x in num_list:
            degree[x] = x

        res = []
        for i in range(n):
            if degree[i] == -1:
                res.append(i)

        if len(res) == 0:
            return edges[0][0]
        elif len(res) > 1:
            return -1
        else:
            return res[0]