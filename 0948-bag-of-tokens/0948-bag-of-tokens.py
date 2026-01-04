class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens:
            return 0
        tokens.sort()
        l, r = 0, len(tokens)-1
        point = 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                point += 1
                l+=1
            elif point > 0 and l < r:
                power += tokens[r]
                point -= 1
                r -= 1
            else:
                break

        return point 
