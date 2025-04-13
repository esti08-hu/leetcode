class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        track = defaultdict(int)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    track[i]+=1
        
        champ = [-1,-1]

        for k,v in track.items():
            if v > champ[1]:
                champ[0] = k
                champ[1] = v
        
        return champ[0]
