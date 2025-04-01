class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            return ''.join('1' if char == '0' else '0' for char in s)

        def generate_sn(n):
            if n == 1:
                return "0"
            
            prev = generate_sn(n - 1)
            return prev + "1" + invert(prev)[::-1] 
        return generate_sn(n)[k-1]