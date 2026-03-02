class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        r = n-1
        j = 0
        rows_0 = []
        for i in range(len(grid)):
            count = 0
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    break
                count += 1
            rows_0.append(count)

        count = 0
        for j in range(n):
            required = n - 1 - j

            target = -1
            for i in range(j, n):
                if rows_0[i] >= required:
                    target = i
                    break
            if target == -1:
                return -1

            while target > j:
                rows_0[target], rows_0[target-1] = rows_0[target-1], rows_0[target]
                target -= 1
                count += 1
                
        return count
