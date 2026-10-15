1class Solution:
2    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
3        arr = [0] * (len(grid) * len(grid))
4        num_set = {i for i in range(1, len(grid) * len(grid)+1)}
5        res = [0, 0]
6        for i in range(len(grid)):
7            for j in range(len(grid)):
8                if arr[grid[i][j] - 1]:
9                    res[0] = grid[i][j]
10                else:
11                    arr[grid[i][j] - 1] = grid[i][j]
12                    num_set.remove(grid[i][j])
13        res[1] = num_set.pop()
14        return res
15