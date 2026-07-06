class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        
        if k > 0:
            for i in range(n):
                total = 0
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
                res[i] = total

        elif k < 0:
            for i in range(n):
                total = 0
                for j in range(1, -k + 1):
                    total += code[(i-j+n)%n]
                res[i] = total

        return res