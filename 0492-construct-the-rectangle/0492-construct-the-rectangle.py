class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = int(math.sqrt(area))

        while area % W != 0:
            W -= 1
        
        L = area // W

        return [L, W]