class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num == math.ceil(sqrt(num))**2