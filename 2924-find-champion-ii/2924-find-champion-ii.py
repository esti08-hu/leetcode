from typing import List
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        num_list = [edge[1] for edge in edges]

        num_set = set(num_list)

        c = [-1]*(n)
        
        for num in num_set:
            c[num] = num
        x = []
        for i in range(n):
            if c[i] == -1:
                x.append(i)
        if len(x) == 0:
            return edges[0][0]
        elif len(x) > 1:
            return -1
        else:
            return x[0]