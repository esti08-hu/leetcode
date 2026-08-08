class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        res = [0] * n
        res[rounds[0]-1] = 1
        diff = 0
        for i in range(1, len(rounds)):
            if rounds[i] < rounds[i-1]:
                diff = n - rounds[i-1] + rounds[i]
            else:
                diff = rounds[i] - rounds[i-1]

            for j in range(rounds[i-1], rounds[i-1] + diff):
                res[j%n] += 1
        
        max_vis = max(res)
        ans = []
        for i in range(len(res)):
            if res[i] == max_vis:
                ans.append(i+1)
        return ans
