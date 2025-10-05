class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache

        def dp(i):
            if i >= len(questions):
                return 0

            take = questions[i][0]+dp(i+questions[i][1]+1)
            skip = dp(i+1)

            return max(take, skip)
        
        return dp(0)
