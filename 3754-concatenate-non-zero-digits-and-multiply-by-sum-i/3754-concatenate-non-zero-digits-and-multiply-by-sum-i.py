class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x_list = []

        while n > 0:
            rem = n%10
            if rem:
                x_list.append(n%10)
            
            n //= 10
        total = sum(x_list)
        m = 1
        x = 0
        for num in x_list:
            x += m*num
            m*=10
        return x * total
