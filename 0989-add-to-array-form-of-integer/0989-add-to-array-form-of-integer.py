class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        total = 0
        d = 1
        for i in range(n-1, -1, -1):
            total += num[i] * d
            d *= 10
        
        res = total + k
        ans = []

        while res > 0:
            ans.append(res%10)
            res //= 10
        
        return ans[::-1]
        
