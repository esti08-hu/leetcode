class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        pick_dict = {i:[0]*11 for i in range(n)}
        
        for p, c in pick:
            pick_dict[p][c]+=1

        count = 0
        for k, v in pick_dict.items():
            for i in range(11):
                if v[i] >= k+1:
                    count += 1
                    break
        return count