class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # [10,3,8,9,4
        # 10 9 8 4 3
        
        score_hash = sorted({score[i]: i for i in range(len(score))}.items(), key=lambda x: x, reverse=True)
        score_hash.sort(reverse=True)
        res = [""] * len(score)
        
        for rank, (s, original_idx) in enumerate(score_hash):
            if rank == 0:
                res[original_idx] = "Gold Medal"
            elif rank == 1:
                res[original_idx] = "Silver Medal"
            elif rank == 2:
                res[original_idx] = "Bronze Medal"
            else:
                res[original_idx] = str(rank + 1)
        
        return res
