class Solution:
        
    def factorial_recursive(self, n):
        if n == 0:
            return 1
        return n * self.factorial_recursive(n - 1)

    def trailingZeroes(self, n: int) -> int:
        sys.set_int_max_str_digits(1000000)

        n = str(self.factorial_recursive(n))
        count = 0

        if n[-1]=="0":
            for i in range(len(n)-1, -1, -1):
                if n[i] == "0":
                    count+=1
                else:
                    break
        return count