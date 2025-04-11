class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            return ''.join('1' if char == '0' else '0' for char in s)

        def generate(n):
            if n == 1:
                return "0"
            
            prev = generate(n - 1)
            return prev + "1" + invert(prev)[::-1] 
        return generate(n)[k-1]